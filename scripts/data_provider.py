#!/usr/bin/python

import MySQLdb
import mysql.connector
import os
import base64
from PipelineAttributes import stages
from selectadb import properties
import subprocess
from PipelineAttributes import default_attributes
import sys

global error_list
error_list=''

	
def get_connection(db_user,db_password,db_host,db_database):
		conn = MySQLdb.connect(user=db_user, passwd=db_password, host=db_host,db=db_database)
		return conn

def get_list(conn):
	stage_name='data_provider'
	query="select process_id,selection_id from process_stages where stage_name='%s'"%stage_name
	cursor = conn.cursor()
	cursor.execute(query)
	
	data_provider_list=list()
	for (process_id, selection_id) in cursor:
		 
		 stage=stages(process_id,selection_id,stage_name)
		 data_provider_list.append(stage)
		
	return data_provider_list


def get_file_names(conn,process_id):
	value=default_attributes.get_attribute_value(conn,'fastq_files',process_id)
	files=list()
	if ";" in value:
		files=value.split(";")
	else:
		files.append(value)
	
	return files
	
def get_datahub_names(conn,process_id):
	value=default_attributes.get_attribute_value(conn,'datahub',process_id)
	return value
	
	
def create_processing_dir(directory):
	if not os.path.exists(directory):
		os.makedirs(directory)


def get_datahub_account_password(conn,account_id):
		query='select password from account where account_id="%s"'%account_id
		cursor = conn.cursor()
		cursor.execute(query)
		for password in cursor:
			passw=password[0]
		return base64.b64decode(passw[::-1])
	


def download_datahub_file(account_name,password,files,outdir):
		for file in files:
			outputfile=outdir+'/'+os.path.basename(file)
			url="ftp://%s:%s@ftp.dcc-private.ebi.ac.uk/data/%s"%(account_name,password,file)
			command="wget -t 2 %s -O %s"%(url,outputfile)
			sp = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
			out, err = sp.communicate()
			if out:
				print "standard output of subprocess:"
				print out
			if err:
				print "standard error of subprocess:"
				print err
			if sp.returncode!=0:
				error_list.append(err)
				print >> sys.stderr, err
		
		

if __name__ == '__main__':
	error_list=list()
	prop=properties('../resources/properties.txt')
	conn=get_connection(prop.dbuser,prop.dbpassword,prop.dbhost,prop.dbname)
	data_provider_list=get_list(conn)
	for data_provider_stage in data_provider_list:
		if data_provider_stage.check_started(conn)==False:
			print "\nTo be started job: process_id:", data_provider_stage.process_id,'collection id:',data_provider_stage.selection_id,'data_provider_stage name:',data_provider_stage.stage_list
			data_provider_stage.set_started(conn)
			process_dir=prop.workdir+data_provider_stage.process_id
			print "Creating process directory:",process_dir
			create_processing_dir(process_dir)
			account_name=get_datahub_names(conn,data_provider_stage.process_id)
			print "account to be processed:",account_name
			files=get_file_names(conn,data_provider_stage.process_id)
			print "Files to be downloaded:",files
			pw=get_datahub_account_password(conn,account_name)
			download_datahub_file(account_name,pw,files,process_dir) 
			if len(error_list)!=0:
				final_errors='\n'.join(error_list) 
				data_provider_stage.set_error(conn,final_errors)
			else:
				data_provider_stage.set_finished(conn)
		error_list=list()
				
	conn.close()
		
		
	
	
	
	
	
	
	
