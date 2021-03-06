import sys
import time


class default_attributes:
    global selection_id_key
    global process_id_key
    global datahub_key
    global tax_id_key
    global scientific_name_key
    global sample_accession_key
    global secondary_sample_acc_key
    global experiment_accession_key
    global study_accession_key
    global secondary_study_acc_key
    global run_accession_key
    global pipeline_name_key
    global provider_center_name_key
    global provider_webin_id_key
    global instrument_platform_key
    global fastq_files_key
    global fastq1_key
    global fastq2_key
    global fastq1_md5_key
    global fastq2_md5_key
    global public_key
    global analyst_webin_id_key
    global pair_key
    global gzip_analysis_file_key
    global gzip_analysis_file_md5_key

    global tab_analysis_file_key
    global tab_analysis_file_md5_key

    global tab_analysis_file2_key
    global tab_analysis_file2_md5_key

    global tab_analysis_file3_key
    global tab_analysis_file3_md5_key

    global tab_analysis_file4_key
    global tab_analysis_file4_md5_key

    global ruler
    ruler = '*' * 100
    selection_id_key = 'selection_id'
    process_id_key = 'process_id'
    datahub_key = 'datahub'
    tax_id_key = 'tax_id'
    scientific_name_key = 'scientific_name'
    sample_accession_key = 'sample_accession'
    secondary_sample_acc_key = 'secondary_sample_acc'
    experiment_accession_key = 'experiment_accession'
    study_accession_key = 'study_accession'
    secondary_study_acc_key = 'secondary_study_acc'
    run_accession_key = 'run_accession'
    pipeline_name_key = 'pipeline_name'
    provider_center_name_key = 'provider_center_name'
    provider_webin_id_key = 'provider_webin_id'
    instrument_platform_key = 'instrument_platform'
    fastq_files_key = 'fastq_files'
    fastq1_key = 'fastq1'
    fastq2_key = 'fastq2'
    fastq1_md5_key = 'fastq1_md5'
    fastq2_md5_key = 'fastq2_md5'
    public_key = 'public'
    analyst_webin_id_key = 'analyst_webin'
    pair_key = 'pair'
    gzip_analysis_file_key = 'gzip_analysis_file'
    gzip_analysis_file_md5_key = 'gzip_analysis_file_md5'
    tab_analysis_file_key = 'tab_analysis_file'
    tab_analysis_file_md5_key = 'tab_analysis_file_md5'

    tab_analysis_file2_key = 'tab_analysis_file2'
    tab_analysis_file2_md5_key = 'tab_analysis_file2_md5'

    tab_analysis_file3_key = 'tab_analysis_file3'
    tab_analysis_file3_md5_key = 'tab_analysis_file3_md5'

    tab_analysis_file4_key = 'tab_analysis_file4'
    tab_analysis_file4_md5_key = 'tab_analysis_file4_md5'


    def __init__(self, process_id, selection_id, datahub, tax_id, scientific_name, sample_accession,
                 secondary_sample_acc, experiment_accession, study_accession, secondary_study_acc, run_accession,
                 pipeline_name, provider_center_name, provider_webin_id, instrument_platform, fastq_files, fastq_md5, public,
                 analyst_webin_id):
        self.process_id = process_id
        self.selection_id = selection_id
        self.datahub = datahub
        self.tax_id = tax_id
        self.scientific_name = scientific_name
        self.sample_accession = sample_accession
        self.secondary_sample_acc = secondary_sample_acc
        self.experiment_accession = experiment_accession
        self.study_accession = study_accession
        self.secondary_study_acc = secondary_study_acc
        self.run_accession = run_accession
        self.pipeline_name = pipeline_name
        self.provider_center_name = provider_center_name
        self.provider_webin_id = provider_webin_id
        self.instrument_platform = instrument_platform
        self.gzip_analysis_file = ''
        self.gzip_analysis_file_md5 = ''
        self.tab_analysis_file = ''
        self.tab_analysis_file_md5 = ''
        self.tab_analysis_file2 = ''
        self.tab_analysis_file2_md5 =''
        self.tab_analysis_file3 = ''
        self.tab_analysis_file3_md5 = ''
        self.tab_analysis_file4 = ''
        self.tab_analysis_file4_md5 = ''


        files = list()
        if ";" in fastq_files:
            #files = fastq_files.split(";")
            files = list(filter(lambda x: '_' in x, fastq_files.split(';')))
            self.fastq1 = files[0]
            self.fastq2 = files[1]
            self.pair = True
        else:
            files.append(fastq_files)
            self.fastq1 = files[0]
            self.fastq2 = ""
            self.pair = False
        self.fastq_files = fastq_files
        md5s = list()
        if ";" in fastq_md5:
            md5s = fastq_md5.split(";")
            self.fastq1_md5 = md5s[0]
            self.fastq2_md5 = md5s[1]
        else:
            md5s.append(fastq_md5)
            self.fastq1_md5 = md5s[0]
            self.fastq2_md5 = ""
        self.public = public
        self.analyst_webin_id = analyst_webin_id

    def __str__(self):
        return 'selection_id:' + str(self.selection_id) + '\n' + 'datahub:' + self.datahub + '\n' + 'tax_id:' + str(
            self.tax_id) + '\n' + \
               'scientific_name:' + self.scientific_name + '\n' + 'sample_accession:' + self.sample_accession + '\n' + \
               'secondary_sample_acc:' + self.secondary_sample_acc + '\n' + 'experiment_accession:' + self.experiment_accession + '\n' + \
               'study_accession:' + self.study_accession + '\n' + 'secondary_study_acc:' + self.secondary_study_acc + '\n' + \
               'run_accession:' + self.run_accession + '\n' + 'pipeline_name:' + self.pipeline_name + '\n' + 'provider_center_name:' + self.provider_center_name + '\n' + \
               'provider_webin_id:' + self.provider_webin_id + '\n' + 'Instrument_platform:' + '\n' + self.instrument_platform + '\n' + 'fastq_files:' + self.fastq_files + '\n' + 'fastq_md5:' + self.fastq_md5 + '\n' + \
               'public:' + self.public + '\n' + 'analyst_webin_id:' + self.analyst_webin_id

    """
    def __str__(self):
        sb = []
        for key in self.__dict__:
            sb.append("{key}='{value}'".format(key=key, value=self.__dict__[key]))

        return ', '.join(sb)
    
    def __repr__(self):
        return self.__str__()

    """

    def insert_into_process_attributes(self, conn, process_id, attribute_key, attribute_value):

        if process_id != "" and attribute_key != "":
            query = "INSERT INTO process_attributes (process_id,attribute_key,attribute_value) values('{}','{}','{}')".format(
                process_id, attribute_key, attribute_value)
            cursor = conn.cursor()
            try:
                print('-'*100)
                print(query)
                print('-'*100)
                cursor.execute(query)
                conn.commit()

            except:
                print("ERROR: Cannot insert:", file=sys.stderr)
                message = str(sys.exc_info()[1])
                print("Exception: %s".format(message), file=sys.stderr)
                conn.rollback()


    def insert_all_into_process_stages(self, conn):
        '''
			insert_all_into_process_stages functions calls on insert_into_process_attributes, shouldnt be the function
		   insert_all_into_process_attributes?
		'''
        print('*' * 100)
        print("insert_all_into_process_stages is called and calls on insert_into_process_attributes")
        print('*' * 100)
        self.insert_into_process_attributes(conn, self.process_id, selection_id_key, self.selection_id)
        self.insert_into_process_attributes(conn, self.process_id, datahub_key, self.datahub)
        self.insert_into_process_attributes(conn, self.process_id, tax_id_key, self.tax_id)
        self.insert_into_process_attributes(conn, self.process_id, scientific_name_key, self.scientific_name)
        self.insert_into_process_attributes(conn, self.process_id, sample_accession_key, self.sample_accession)
        self.insert_into_process_attributes(conn, self.process_id, secondary_sample_acc_key, self.secondary_sample_acc)
        self.insert_into_process_attributes(conn, self.process_id, experiment_accession_key, self.experiment_accession)
        self.insert_into_process_attributes(conn, self.process_id, study_accession_key, self.study_accession)
        self.insert_into_process_attributes(conn, self.process_id, secondary_study_acc_key, self.secondary_study_acc)
        self.insert_into_process_attributes(conn, self.process_id, run_accession_key, self.run_accession)
        self.insert_into_process_attributes(conn, self.process_id, pipeline_name_key, self.pipeline_name)
        self.insert_into_process_attributes(conn, self.process_id, provider_center_name_key, self.provider_center_name)
        self.insert_into_process_attributes(conn, self.process_id, provider_webin_id_key, self.provider_webin_id)
        self.insert_into_process_attributes(conn, self.process_id, instrument_platform_key, self.instrument_platform)
        self.insert_into_process_attributes(conn, self.process_id, fastq_files_key, self.fastq_files)
        self.insert_into_process_attributes(conn, self.process_id, fastq1_key, self.fastq1)
        self.insert_into_process_attributes(conn, self.process_id, fastq2_key, self.fastq2)
        self.insert_into_process_attributes(conn, self.process_id, fastq1_md5_key, self.fastq1_md5)
        self.insert_into_process_attributes(conn, self.process_id, fastq2_md5_key, self.fastq2_md5)
        self.insert_into_process_attributes(conn, self.process_id, public_key, self.public)
        self.insert_into_process_attributes(conn, self.process_id, analyst_webin_id_key, self.analyst_webin_id)

        self.insert_into_process_attributes(conn, self.process_id, gzip_analysis_file_key, self.gzip_analysis_file)
        self.insert_into_process_attributes(conn, self.process_id, gzip_analysis_file_md5_key, self.gzip_analysis_file_md5)

        self.insert_into_process_attributes(conn, self.process_id, tab_analysis_file_key, self.tab_analysis_file)
        self.insert_into_process_attributes(conn, self.process_id, tab_analysis_file_md5_key, self.tab_analysis_file_md5)

        self.insert_into_process_attributes(conn, self.process_id, tab_analysis_file2_key, self.tab_analysis_file2)
        self.insert_into_process_attributes(conn, self.process_id, tab_analysis_file2_md5_key, self.tab_analysis_file2_md5)

        self.insert_into_process_attributes(conn, self.process_id, tab_analysis_file3_key, self.tab_analysis_file3)
        self.insert_into_process_attributes(conn, self.process_id, tab_analysis_file3_md5_key, self.tab_analysis_file3_md5)

        self.insert_into_process_attributes(conn, self.process_id, tab_analysis_file4_key, self.tab_analysis_file4)
        self.insert_into_process_attributes(conn, self.process_id, tab_analysis_file4_md5_key, self.tab_analysis_file4_md5)

        self.insert_into_process_attributes(conn, self.process_id, pair_key, self.pair)

    @staticmethod
    def get_attribute_value(conn, attribute_key, process_id):
        query = "select attribute_value from process_attributes where attribute_key='{}' and process_id='{}' ".format(
            attribute_key, process_id)
        cursor = conn.cursor()
        cursor.execute(query)
        #cursor.close()
        for attribute_value in cursor:
            value = attribute_value
        #return value[0]
        return str(''.join(value))

    @staticmethod
    def get_all_attributes(conn, process_id):
        query = "select attribute_key,attribute_value from process_attributes where process_id='{}' ".format(process_id)
        cursor = conn.cursor()
        cursor.execute(query)
        #cursor.close()
        key_value = dict()
        for attribute_key, attribute_value in cursor:
            key_value[attribute_key] = attribute_value
        # print attribute_key,attribute_value
        return key_value


class stages:
    global selection_id_key
    global process_id_key
    global stage_name_key
    # global process_report_id_key

    selection_id_key = 'selection_id'
    process_id_key = 'process_id'
    # process_report_id_key = 'process_report_id'
    stage_name_key = 'stage_name'

    data_provider_stage_name = 'data_provider'
    core_executor_stage_name = 'core_executor'
    analysis_reporter_stage_name = 'analysis_reporter'
    process_archival_stage_name = 'process_archival'

    def __init__(self, process_id, selection_id, stage_list):  # process_report_id,
        self.process_id = process_id
        self.selection_id = selection_id
        # self.process_report_id = process_report_id
        self.stage_list = stage_list


    def process_report_set_finished(self, conn):
        """" info is a dict with the following:
    		 process_archival.py add the finish date to end_time
    	"""
        query = "update process_report set process_report_end_time=NOW() where process_id='{}'".format(self.process_id)
        print(query)
        cursor = conn.cursor()
        try:
            cursor.execute(query)
            conn.commit()
            #cursor.close()
        except:
            print("ERROR: can not set process_report_end_time to NOW():", file=sys.stderr)
            message = str(sys.exc_info()[1])
            print("Exception: {}".format(message), file=sys.stderr)
            conn.rollback()
            #cursor.close()


    def insert_into_process_stages(self, conn, process_id, selection_id, stage_name):
        print("Insert to process_stages:", process_id, selection_id, stage_name)
        query = "INSERT INTO process_stages (process_id,selection_id,stage_name) values('{}','{}','{}')".format(
            process_id, selection_id, stage_name)
        print(ruler, "\nInsert into process stage:\n\t{}".format(query), '\n', sep="")
        cursor = conn.cursor()
        try:
            cursor.execute(query)
            conn.commit()
            #cursor.close()
        except:
            print("ERROR: INSERT INTO process_stages table: {}".format(query), file=sys.stderr)
            message = str(sys.exc_info()[1])
            print("Exception: {} : {}".format(message, query), file=sys.stderr)
            conn.rollback()
            #cursor.close()

    def insert_all_into_process_stages(self, conn):
        for stage in self.stage_list:
            self.insert_into_process_stages(conn, self.process_id, self.selection_id, stage)

    def check_started(self, conn):
        query = "select distinct process_id from process_stages where stage_start is null and stage_name='{}'".format(
            self.stage_list)
        cursor = conn.cursor()
        process_id_all=list()
        try:
            cursor.execute(query)
        except:
            print("ERROR: SELECT PROCESS_ID: {}".format(query), file=sys.stderr)
            message = str(sys.exc_info()[1])
            print("Exception: {} : {}".format(message, query), file=sys.stderr)
            conn.rollback()
            #cursor.close()
        for row in cursor:
            process_id_all.append(row[0])
            #cursor.close()
        if self.process_id in process_id_all:
            #cursor.close()
            return False
        else:
            #cursor.close()
            return True

    def set_started(self, conn):
        query = "update process_stages set stage_start=NOW() where process_id='{}' and stage_name='{}'".format(
            self.process_id, self.stage_list)

        cursor = conn.cursor()
        try:
            print('-'*100)
            print(query)
            print('-'*100)
            cursor.execute(query)
            conn.commit()
            #cursor.close()

        except (MySQLdb.Error, MySQLdb.Warning) as e:
            print("ERROR: Cannot update process_stages set stage_start=NOW():", file=sys.stderr)
            message = str(sys.exc_info()[1])
            print("Exception: {}, {}".format(message, e), file=sys.stderr)
            print('-'*100)
            print("MySQL error: {}".format(e))
            print('-'*100)
            conn.rollback()

    def set_finished(self, conn):
        query = "update process_stages set stage_end=NOW() where process_id='{}' and stage_name='{}'".format(
            self.process_id, self.stage_list)
        cursor = conn.cursor()
        try:
            cursor.execute(query)
            conn.commit()
            #cursor.close()

        except:
            print("ERROR: Cannot update process_stages set stage_end=NOW():", file=sys.stderr)
            message = str(sys.exc_info()[1])
            print("Exception: {}".format(message), file=sys.stderr)
            conn.rollback()

    def set_error(self, conn, error):
        query = ("update process_stages set stage_error='{}'"
                 " where process_id='{}'"
                 " and stage_name='{}'").format(error, self.process_id, self.stage_list)
        print('*' * 100)
        print("SET_ERROR QUERY:\n{}".format(query))
        print('*' * 100)
        cursor = conn.cursor()
        try:
            cursor.execute(query)
            conn.commit()
            #cursor.close()

        except:
            print("ERROR: Cannot {}".format(query), file=sys.stderr)
            message = str(sys.exc_info()[1])
            print("Exception: {}".format(message), file=sys.stderr)
            conn.rollback()


