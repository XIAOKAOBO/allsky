#
# Configuration file for webdata generator
# 

MYSQL_HOST = '192.168.8.1'
MYSQL_USER = 'allsky'
MYSQL_PASSWORD = 'allsky'
MYSQL_DB = 'allsky'

MYSQL_DB_SIMEIZ = 'cloudsensor_simeiz'

### system report ###

BOARD_MODEL_FILE = '/proc/device-tree/model'
OS_RELEASE_FILE = '/etc/os-release'

QHY_CAM_BIN = '/opt/allsky/bin/qhy_camera'

SYSTEM_HTML_TEMPLATE = '/storage/web/system.html.tpl'
SYSTEM_HTML_RESULT = '/storage/webdata/system.html'

PLOT_DISKS_USAGE = '/storage/webdata/disks_usage.png'

###

### system sensors

PLOT_CPU_TEMPERATURE_DAY = '/storage/webdata/cpu_temperature_day.png'
PLOT_INTERNAL_DH22_DAY = '/storage/webdata/internal_dh22_day.png'

###

### sensor graphgen ###

PLOT_CLOUD_SENSOR_DAY = '/storage/webdata/cloud_sensor_day.png'
CSV_CLOUD_SENSOR_DAY = '/storage/webdata/cloud_sensor_day.csv'

PLOT_CLOUD_SENSOR_DAY_SIMEIZ = '/storage/webdata/cloud_sensor_day_simeiz.png'
CSV_CLOUD_SENSOR_DAY_SIMEIZ = '/storage/webdata/cloud_sensor_day_simeiz.csv'


PLOT_CLOUD_SENSOR_WEEK = '/storage/webdata/cloud_sensor_week.png'
CSV_CLOUD_SENSOR_WEEK = '/storage/webdata/cloud_sensor_week.csv'

PLOT_CLOUD_SENSOR_WEEK_SIMEIZ = '/storage/webdata/cloud_sensor_week_simeiz.png'
CSV_CLOUD_SENSOR_WEEK_SIMEIZ = '/storage/webdata/cloud_sensor_week_simeiz.csv'


PLOT_CLOUD_SENSOR_MONTH = '/storage/webdata/cloud_sensor_month.png'
CSV_CLOUD_SENSOR_MONTH = '/storage/webdata/cloud_sensor_month.csv'

PLOT_CLOUD_SENSOR_MONTH_SIMEIZ = '/storage/webdata/cloud_sensor_month_simeiz.png'
CSV_CLOUD_SENSOR_MONTH_SIMEIZ = '/storage/webdata/cloud_sensor_month_simeiz.csv'


PLOT_CLOUD_SENSOR_YEAR = '/storage/webdata/cloud_sensor_year.png'
CSV_CLOUD_SENSOR_YEAR = '/storage/webdata/cloud_sensor_year.csv'

PLOT_CLOUD_SENSOR_YEAR_SIMEIZ = '/storage/webdata/cloud_sensor_year_simeiz.png'
CSV_CLOUD_SENSOR_YEAR_SIMEIZ = '/storage/webdata/cloud_sensor_year_simeiz.csv'


PLOT_EXTERNAL_DH22_DAY = '/storage/webdata/external_dh22_day.png'
CSV_EXTERNAL_DH22_DAY = '/storage/webdata/external_dh22_day.csv'

PLOT_AMBIENT_SENSOR_DAY_SIMEIZ = '/storage/webdata/ambient_sensor_day_simeiz.png'
CSV_AMBIENT_SENSOR_DAY_SIMEIZ = '/storage/webdata/ambient_sensor_day_simeiz.csv'


PLOT_EXTERNAL_DH22_WEEK = '/storage/webdata/external_dh22_week.png'
CSV_EXTERNAL_DH22_WEEK = '/storage/webdata/external_dh22_week.csv'

PLOT_AMBIENT_SENSOR_WEEK_SIMEIZ = '/storage/webdata/ambient_sensor_week_simeiz.png'
CSV_AMBIENT_SENSOR_WEEK_SIMEIZ = '/storage/webdata/ambient_sensor_week_simeiz.csv'


PLOT_EXTERNAL_DH22_MONTH = '/storage/webdata/external_dh22_month.png'
CSV_EXTERNAL_DH22_MONTH = '/storage/webdata/external_dh22_month.csv'

PLOT_AMBIENT_SENSOR_MONTH_SIMEIZ = '/storage/webdata/ambient_sensor_month_simeiz.png'
CSV_AMBIENT_SENSOR_MONTH_SIMEIZ = '/storage/webdata/ambient_sensor_month_simeiz.csv'


PLOT_EXTERNAL_DH22_YEAR = '/storage/webdata/external_dh22_year.png'
CSV_EXTERNAL_DH22_YEAR = '/storage/webdata/external_dh22_year.csv'

PLOT_AMBIENT_SENSOR_YEAR_SIMEIZ = '/storage/webdata/ambient_sensor_year_simeiz.png'
CSV_AMBIENT_SENSOR_YEAR_SIMEIZ = '/storage/webdata/ambient_sensor_year_simeiz.csv'


PLOT_AMBIENT_LIGHT_DAY = '/storage/webdata/ambient_light_day.png'
CSV_AMBIENT_LIGHT_DAY = '/storage/webdata/ambient_light_day.csv'

PLOT_AMBIENT_LIGHT_WEEK = '/storage/webdata/ambient_light_week.png'
CSV_AMBIENT_LIGHT_WEEK = '/storage/webdata/ambient_light_week.csv'

PLOT_AMBIENT_LIGHT_MONTH = '/storage/webdata/ambient_light_month.png'
CSV_AMBIENT_LIGHT_MONTH = '/storage/webdata/ambient_light_month.csv'

PLOT_AMBIENT_LIGHT_YEAR = '/storage/webdata/ambient_light_year.png'
CSV_AMBIENT_LIGHT_YEAR = '/storage/webdata/ambient_light_year.csv'

###

WEB_SKYTEMP_FILE = '/storage/webdata/sky_temp.txt'
WEB_CURRENT_COND_FILE = '/storage/webdata/current_cond.txt'
WEB_OUT_TEMP_FILE = '/storage/webdata/air_temp.txt'
WEB_OUT_HUMID_FILE = '/storage/webdata/air_humid.txt'

WEB_SKYTEMP_SIMEIZ_FILE = '/storage/webdata/sky_temp_simeiz.txt'
WEB_CURRENT_COND_SIMEIZ_FILE = '/storage/webdata/current_cond_simeiz.txt'
WEB_OUT_TEMP_SIMEIZ_FILE = '/storage/webdata/air_temp_simeiz.txt'
WEB_OUT_HUMID_SIMEIZ_FILE = '/storage/webdata/air_humid_simeiz.txt'

###

### cloud air datagen ###

PLOT_SKY_AIR_TEMP = '/storage/webdata/sky_air_temp.png'
WEB_OUT_TDELTA_FILE = '/storage/webdata/sky_air_delta.txt'
WEB_OUT_TMM_FILE = '/storage/webdata/sky_max_min.txt'

