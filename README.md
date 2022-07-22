## CHIME/SPS

### How to run
- Make sure flask is installed
- Inside the home directory run 
```commandline bash
python app.py
```

### REST End points 

- **GET** -- '/'  
- **GET**  --'/radioobjects' 
- **POST** -- '/radioobjects' 
  - Make sure you pass Content-Type header to application/json


## Next Steps 
- The REST app is not finished completely
- TODO: 
  - Implement the PUT, DELETE methods
  - Create radioastrophysicalobject and save to the dictonary
  - Implement validations in radioastrophysicalobject type, dispersion etc..
  - 

