# RPI PowerMeter 

## Setup

 * Install Raspbian
   * Setup Networking, Wifi or Ethernet (Recomended)
   * Setup SSH (Recomended)
   * Setup avahi daemon (Recomended)

 * Install Docker

   ~~~
   curl https://get.docker.com | sh
   ~~~

 * Install docker-compose
   
   ~~~
   pip3 install docker-compose
   ~~~

## Configuration

 * Create InfluxDB Database and powermeter
 * Configure Grafana users, datasource, and graphs


## Backups:

 * Data is persisted on volumes and generaly on /var/lib/docker/volumes/
