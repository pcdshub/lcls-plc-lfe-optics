IOC_TOP = /reg/g/pcds/epics/ioc/common/ads-ioc/R0.6.1
IOC_INSTANCE_PATH := $(shell pwd)

# Set PRODUCTION_IOC to 1 to move from a testing to a production IOC:
PRODUCTION_IOC := 1

PROJECT_NAME := lcls-plc-lfe-optics
PROJECT_PATH := ../../lcls-plc-lfe-optics/lcls-plc-lfe-optics.tsproj
PLC := lfe_optics

PYTMC_OPTS := 
PREFIX := PLC:LFE:OPTICS

include $(IOC_TOP)/iocBoot/templates/Makefile.base
