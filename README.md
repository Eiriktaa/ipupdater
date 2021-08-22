# Ipupdater

Updates the ip records on a cloudflare DNS, after public ip changes, designed to be run a cronscript on a webhost that does not have a static ip

| Environment variables|  |   
|---|---|
| CLOUDFLARE_ZONE  |  The zone id connected to your domainadress on cloudflare |
|  CLOUDFLARE_EMAIL | Email adress attached to your cloudflare account  |
| CLOUDFLARE_TOKEN  | An api token with Zone:read and DNS:Edit permissions  |
