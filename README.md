# invalid_path_identifier

python script to identify invalid windows system path

## error
    "The System Cannot Find The Path Specified" (EN)
    "Das System kann den angegebenen Pfad nicht finden." (DE)

![](example_error.png)

## usage
`python invalid_path_identifier.py`

the script returns: the path variable number + invalid path

![](example_match01.png)

## steps to resolve the error

which can be found and removed through

    WIN-Key + R
    rundll32.exe sysdm.cpl,EditEnvironmentVariables

or via mouse

    WIN-Key -> SystemEnvironment Variables (EN)
    -> Environment Variables...
    
    WIN-Taste -> Systemumgebunsvariablen bearbeiten (DE)
    -> Umgebungsvariablen
    
![](system_properties-advanced-environment_variables.png) ![](systemeigenschaften-erweitert-umgebungsvariablen.png)
    

select the top entry, click ARROW-DOWN as much times as the number says

in the example 29 times

![](example_match01_29.png)
