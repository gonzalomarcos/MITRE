
<!-- ABOUT THE PROJECT -->
## About The Project

This script extracts all techniques present in the evaluation's json of a participant from a directory and output as csv format. You can download all the techniques from [MITRE ENGENUITY](https://attackevals.mitre-engenuity.org/). **It will only extract the TTPs covered as "Technique"**.





<!-- USAGE -->
## USAGE

1. Go to a participant evaluation, for example [Elastic]https://attackevals.mitre-engenuity.org/enterprise/participants/elastic?view=overview&adversary=wizard-spider-sandworm)
![Participants](https://github.com/gonzalomarcos/Personal/blob/master/mitre-engenuity/Participants.PNG)

2. Chose all the evaluations you want and place it to a directory

3. Execute
   ```sh
   EDR.py > output.csv
   ```
