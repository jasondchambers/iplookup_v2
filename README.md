# iplookup

This component, when integrated through the [External Lookup](https://www.cisco.com/c/dam/en/us/td/docs/security/stealthwatch/management_console/external_lookup/7_4_External_Lookup_DV_1_0.pdf) feature of [Cisco Secure Network Analytics](https://www.cisco.com/c/en/us/products/security/stealthwatch/index.html) enables the user to lookup an internal IP details by redirecting to the Meraki Dashboard.

This component is available for use by the Cisco DevNet community through Code Exchange.

## Requirements
1. Docker (this component is built and run as a Docker container)
2. Cisco Secure Network Analytics 7.4.0 and above
3. Meraki MX 
4. A server where the container can run 

## Installation
Installation involves configuration, build and run followed by configuration of the External Lookup feature within Cisco Secure Network Analytics.

To get started with the installation, simply clone this project (assuming Git is installed) then move on to the "Configuration" step. 

## Configuration
Modify the `Dockerfile` as guided (these pieces of information can be found logging into the Meraki Dashboard):
```
ENV api_key YOUR_MERAKI_API_KEY_GOES_HERE
ENV network_id YOUR_MERAKI_NETWORK_ID_KEY_GOES_HERE
```
> **Note:** To obtain your Meraki API key, please follow these steps: https://documentation.meraki.com/zGeneral_Administration/Other_Topics/The_Cisco_Meraki_Dashboard_API

Decide which port the service is to listen on - the default is 5001. Modify the run.sh script if there is a requirement to use a different port and map it to the container port of 5001.

Now continue to the "Build" step.

## Build and Run
Once configured, build the Docker image as follows:
```
./build.sh
```
Once built, run the Docker container as follows:
```
./run.sh
```

## Cisco Secure Network Analytics Configuration
The next step is configure the External Lookup Feature in Cisco Network Analytics.

Instructions for how to do this can be found in the [Cisco Secure Network Analytics documentation.] 
(https://www.cisco.com/c/dam/en/us/td/docs/security/stealthwatch/management_console/external_lookup/7_4_External_Lookup_DV_1_0.pdf)


## Testing

TODO

## Debugging
The logs can be viewed as follows:
```
tail -f nohup.out
```
The component can be tested quickly by pointing your browser to:
```
http://localhost:5001/iplookup/?ipaddress=192.168.128.160
```

## Developing
This step is optional and is for those who wish to modify the code to suit their specific needs. Please review the "Getting Involved" section below"

Deployment is based on Docker and containerization - however, development and unit testing is not. For development, we use Python's Virtual Environment feature. You can set this up by running this script: 
```
./createvenv.sh
```

Now, we can run the unit tests as follows:

```
./unittest.sh
```

### Structure

TODO

## Getting Involved
Contributions to this code are welcome and appreciated... see [CONTRIBUTING](CONTRIBUTING.md) for details... 

Please adhere to our [Code of Conduct](CODE_OF_CONDUCT.md) at all times

## Licensing info
This code is licensed under the BSD 3-Clause License... see [LICENSE](LICENSE) for details

[![published](https://static.production.devnetcloud.com/codeexchange/assets/images/devnet-published.svg)](https://developer.cisco.com/codeexchange/github/repo/yzxbmlf/ipblock)
