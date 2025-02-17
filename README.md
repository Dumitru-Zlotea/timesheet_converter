# timesheet_converter

Converts worked hours logged in the format

    monday 30: 10h30 - 11h00
    14h15 - 15h00
    tuesday 01: 13h00 - 13h40
    15h50 - 17h25
    tuesday 01 (PROJECT_CODE): 17h30 - 19h00
    ...

To

    monday 30:    1.25
    tuesday 01:   2.25
    tuesday 01 (PROJECT_CODE): 1.5
    ...
    total ->      X.XX

The input hours should be in a text file _work_hours.txt_ in the same directory as the python script.  
The output will be generated in a new file called _result.txt_
