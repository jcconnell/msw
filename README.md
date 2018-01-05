# msw

## Introduction
msw is a tool that uses the Magicseaweed forecast api to automatically check the surf forecast of all user specified surf breaks. The tool reports back any surf spots where the surf forecast is at least a solid 3 stars.

Keep in mind to use the msw tool you will need apply for a personal API key. That and more information regarding the Magicseaweed api can be found [here](https://magicseaweed.com/developer/api).

## Configuring msw
Use config_msw.yml to configure the msw tool. In this yaml file you can define a number of user preferences:

* Your personal API key
* Surf Spots you want to check
* The days you wish to surf

## Usage
Running spotCheck.py will then return all surf spots where the surf forecast is at least a solid 3 stars and the forecasted day matches those days specified in config_msw.yml.

## Dependancies
Some Python packages are used in this code:

* [Pandas](https://pandas.pydata.org/pandas-docs/stable/)
* [PyYaml](https://github.com/yaml/pyyaml)

## Issue Guidlines
In case you encounter bugs please submit a new issue on [github](https://github.com/HowardRiddiough/msw/issues). Please list the reported error and data used that will help us reconstruct it. This will help us reproduce and resolve the bug.

## Contributors
[HowardRiddiough](https://github.com/HowardRiddiough)