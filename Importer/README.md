# The Importer
## Features
There abilities as:

* Add partner with asset files.
* View all partners
* Delete partner
* Update partner
* Configurable with config.json
** Set service port number
** Set upload folder
** Set type of the allowed
1) Type of extension
2) Target folder of the extension
3) Type of sheet

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
### For users
* View all

```
http://localhost:8000/
```
![Alt text](https://github.com/samat/JustShared/blob/master/Importer/demo/view.png "Optional Title")

* Add patner
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


