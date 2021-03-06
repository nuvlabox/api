# Changelog
## [1.2.0] - 2021-02-12
### Added
### Changed
 - deprecate HOST_USER in favor of HOME
## [1.1.1] - 2021-01-12
### Added
### Changed
 - ensure existing streaming containers are deleted on duplicated requests
## [1.1.0] - 2021-01-12
### Added 
 - upgraded data-source-mjpg container 
 - additional logging
### Changed
 - reduced number of api workers
## [1.0.0] - 2021-01-08
### Added 
 - auto-restart on docker-proxy failure
### Changed
## [0.4.0] - 2020-12-04
### Added 
  - re-use persisted env vars
### Changed
  - minor fixes
## [0.3.2] - 2020-10-02
### Added 
- ONBUILD SixSq license dump
### Changed
## [0.3.1] - 2020-08-10
### Added
### Changed
- removed file logging
## [0.3.0] - 2020-07-28
### Added 
- new API call for restarting a video stream
### Changed
- refactored functions that are re-used in multiple API calls
## [0.2.0] - 2020-06-23
### Added 
- New API calls and workflow to manage SSH keys on the host
### Changed
## [0.1.0] - 2020-03-13
### Added 
- API endpoints for enabling and disabling MJPG streaming from USB devices
### Changed
## [0.0.2] - 2020-02-18
### Added
### Changed
- re-use compute-api ssl certificates instead of generating our own

## [0.0.1] - 2020-02-17
### Added
- first minimal version of the mgmt api
### Changed
