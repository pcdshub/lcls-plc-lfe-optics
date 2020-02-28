IOC_TOP = /reg/g/pcds/epics/ioc/common/ads-ioc/R0.2.1
IOC_INSTANCE_PATH := $(shell pwd)

# Set PRODUCTION_IOC to 1 to move from a testing to a production IOC:
PRODUCTION_IOC := 1

PROJECT_NAME := MR1L0-MR2L0
PROJECT_PATH := ../../MR1L0-MR2L0/MR1L0-MR2L0.tsproj
PLC := MR1L0_MR2L0_PLC

PYTMC_OPTS := 
PREFIX := PREFIX

include $(IOC_TOP)/iocBoot/templates/Makefile.base
