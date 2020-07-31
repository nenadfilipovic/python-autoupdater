# Python autoupdater

Script that check user defined github repository for new version of firmware, then downloads it and remove old one.

Created for using with esp32/esp8266 boards in mind.

## Getting Started

Clone this repository

```
git clone https://github.com/nenadfilipovic/python-autoupdater
```

### Prerequisites

In script user needs to define repository url and root folder name which should be in same directory as script.

### Installing

Change database data in config.php with your database data and create user.
Put the script in same directory with root directory that you defined in script. Script will ask to create version file if it is not in root directory and to give it value. You should create release for your repository and give it semantic version.

## Running the tests

At start script check local and remote versions and if needed download new version and remove old. After updating script continue to run user defined script or project.

### Break down into end to end tests

-

### And coding style tests

-

## Deployment

-

## Built With

* [Python](https://www.python.org/)

## Authors

* **Nenad Filipovic** - *Initial work* - [nenadfilipovic](https://github.com/nenadfilipovic)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

-
