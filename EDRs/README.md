
<!-- ABOUT THE PROJECT -->
## About The Project

This script transforms a csv file to a nested YAML.

You will need a csv with the following fields. 

![csvMitre](https://github.com/gonzalomarcos/Personal/blob/master/EDRs/csvMitre.PNG)

CSV fields:
* Tecnica/Technique: Name of the technique ID
* ID: ID of a MITRE TTP
* Familia/Family: Info about the detection rule or where its saved (SIEM, Defender, Splunk..) :smile:
* Valor/Value: A number between 0-1. You can set an x if you don't want to consider it. The script will pass.

Once you run it, you will hace the same output as if you create the file from [DeTT&CT Editor](https://rabobank-cdc.github.io/dettect-editor/#/techniques) and ready to run DeTTECT scripts.


<!-- USAGE -->
## USAGE

You will have to set the input csv and the output YAML, just edit the script lines 8 and 9 of MITREEDR.py and run it.

![codeMitre](https://github.com/gonzalomarcos/Personal/blob/master/EDRs/codeMitre.PNG)



1. Execute
   ```sh
   MITREEDR.py
   ```
