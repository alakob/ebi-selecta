-- MySQL Script generated by MySQL Workbench
-- Tue Nov 22 22:47:07 2016
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema selectadb
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `selectadb` ;

-- -----------------------------------------------------
-- Schema selectadb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `selectadb` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci ;
USE `selectadb` ;

-- -----------------------------------------------------
-- Table `selectadb`.`cv_pipelines`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `selectadb`.`cv_pipelines` ;

CREATE TABLE IF NOT EXISTS `selectadb`.`cv_pipelines` (
  `pipeline_id` INT NOT NULL COMMENT '',
  `pipline_name` VARCHAR(200) NULL COMMENT '',
  `pipeline_desc` VARCHAR(1000) NULL COMMENT '',
  `pipeline_properties` VARCHAR(500) NULL COMMENT '',
  PRIMARY KEY (`pipeline_id`)  COMMENT '',
  UNIQUE INDEX `pipline_name_UNIQUE` (`pipline_name` ASC)  COMMENT '')
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `selectadb`.`process_stages`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `selectadb`.`process_stages` ;

CREATE TABLE IF NOT EXISTS `selectadb`.`process_stages` (
  `process_id` INT NOT NULL COMMENT '',
  `pipeline_id` INT NOT NULL COMMENT '',
  `stage_name` VARCHAR(100) NOT NULL COMMENT '',
  `audit_time` TIMESTAMP NULL COMMENT '',
  `audit_user` VARCHAR(100) NULL COMMENT '',
  `stage_start` DATETIME NULL COMMENT '',
  `stage_end` DATETIME NULL COMMENT '',
  `stage_error` VARCHAR(1000) NULL COMMENT '',
  PRIMARY KEY (`stage_name`, `process_id`)  COMMENT '')
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `selectadb`.`account`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `selectadb`.`account` ;

CREATE TABLE IF NOT EXISTS `selectadb`.`account` (
  `account_id` VARCHAR(16) NOT NULL COMMENT '',
  `email` VARCHAR(255) NULL COMMENT '',
  `password` VARCHAR(32) NOT NULL COMMENT '',
  `account_type` TIMESTAMP NOT NULL COMMENT '',
  PRIMARY KEY (`account_id`)  COMMENT '');


-- -----------------------------------------------------
-- Table `selectadb`.`process_selection`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `selectadb`.`process_selection` ;

CREATE TABLE IF NOT EXISTS `selectadb`.`process_selection` (
  `account_id` VARCHAR(100) NOT NULL COMMENT '',
  `tax_id` INT NULL COMMENT '',
  `study_accession` VARCHAR(45) NULL COMMENT '',
  `run_accession` VARCHAR(45) NULL COMMENT '',
  `pipeline_name` VARCHAR(200) NOT NULL COMMENT '',
  `analysis_id` VARCHAR(45) NULL COMMENT '',
  `selection_id` VARCHAR(45) NOT NULL COMMENT '',
  `selection_provided_date` DATETIME NULL COMMENT '',
  `selection_to_info_start` DATETIME NULL COMMENT '',
  `selection_to_info_end` DATETIME NULL COMMENT '',
  `selection_to_info_error` VARCHAR(300) NULL COMMENT '',
  `audit_time` VARCHAR(45) NULL COMMENT '',
  `audit_user` VARCHAR(45) NULL COMMENT '',
  PRIMARY KEY (`selection_id`)  COMMENT '')
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `selectadb`.`process_attributes`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `selectadb`.`process_attributes` ;

CREATE TABLE IF NOT EXISTS `selectadb`.`process_attributes` (
  `process_id` INT NOT NULL COMMENT '',
  `attribute_key` VARCHAR(100) NULL COMMENT '',
  `attribute_value` VARCHAR(200) NULL COMMENT '')
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `selectadb`.`selecta_rule_templates`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `selectadb`.`selecta_rule_templates` ;

CREATE TABLE IF NOT EXISTS `selectadb`.`selecta_rule_templates` (
  `template_id` INT NOT NULL COMMENT '',
  `pipeline_id` VARCHAR(45) NULL COMMENT '',
  `template` VARCHAR(45) NULL COMMENT '',
  `master_attributes` VARCHAR(45) NULL COMMENT '',
  `all_attributes` VARCHAR(45) NULL COMMENT '',
  PRIMARY KEY (`template_id`)  COMMENT '')
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
