# The Importer
Here is a tiny project for demo only

## Features
The below are the abilities of the system

* Add partner with asset files.
* View all partners
* Delete partner
* Update partner
* Configurable with config.json
  * Set service port number
  * Set upload folder
  * Set type of the allowed
    * Type of extension
    * Target folder of the extension
    * Type of sheet

## Implementation

### Front-end
* Use Flask framework
* Use html templates
* Use the Bootstrap framework

### Back-end
* Use Flask framework
* Implement as RestFUL web service
* SQLite 3
* ORM by Weepee

## Usage
### For the new installation
```
python create_partner_db.py
```
### For the tests
```
python svcTestCase.py
```

### For users
To run the system
```
python svc.py
```

* View all

```
http://localhost:8000/
```
![Alt text](https://github.com/samat/JustShared/blob/master/Importer/demo/view.png "Optional Title")

* Add partner
```
http://localhost:8000/update-partner
```
![Alt text](https://github.com/samat/JustShared/blob/master/Importer/demo/create.png "Optional Title")

```
http://localhost:8000/update-partner
```

### RestFUL Web Service APIs
* Read
```
http://localhost:8000/read/<name>
```
![Alt text](https://github.com/samat/JustShared/blob/master/Importer/demo/svc-read.png "Optional Title")

* Create
```
http://localhost:8000/create/<name>/<slug>/<active>/<path:spread_sheet_path>/<path:image_path>
```

* Update
```
http://localhost:8000/update/<name>/<slug>/<active>/<path:spread_sheet_path>/<path:image_path>
```

* Delete
```
http://localhost:8000//delete/<name>
```


