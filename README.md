# msw

## Introduction
msw is a tool that uses the Magicseaweed forecast api to create a web based geographic visulisation of the current surf forecast. The website can be found [here](https://howardriddiough.github.io/msw/).

The visulisation includes a bubble for every surf spot listed in [surf_spots.csv](https://github.com/HowardRiddiough/msw/blob/master/data/surfspots.csv). The size of the bubble is determined by the actual wave height and the bubble's color intensity determined by the number of solid stars as provided by Magicseaweed. Each bubble can be clicked to show more information about the surf spot and it's respective foreacst. The idea being to show clearly in one view where the best location to surf at a given moment in time is.

msw is powered by Magicseaweed's forecast api, more information can be found [here](https://magicseaweed.com/developer/api).

## Work in progress
msw is very much a work in progress. There are a number of things to be added to the tool:

* All surf spots need to be added to surf_spots.csv.
* An arrow indicating local wind direction is to be added to the map.
* Ideally some tidal information would be included in the map too.
* Time dimesion to be added so users can see how the forecast develops over the coming days.

## Usage
Running spotCheck.py will create [index.html](https://github.com/HowardRiddiough/msw/blob/master/index.html).

## Dependancies
In order to run this code you will need to have the following packages:

* [os](https://docs.python.org/2/library/os.html)
* [datetime](https://docs.python.org/2/library/datetime.html)
* [Pandas](https://pandas.pydata.org/pandas-docs/stable/)
* [matplotlib](https://matplotlib.org/contents.html)
* [PyYaml](https://github.com/yaml/pyyaml)
* [Folium](https://github.com/python-visualization/folium)
* [webbrowser](https://docs.python.org/2/library/webbrowser.html)

## Issue Guidlines
In case you encounter bugs please submit a new issue on [github](https://github.com/HowardRiddiough/msw/issues). Please list the reported error and data used that will help us reconstruct it. This will help us reproduce and resolve the bug.

## Contributors
[HowardRiddiough](https://github.com/HowardRiddiough)