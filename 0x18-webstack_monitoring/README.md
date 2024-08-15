# 0x18. Webstack monitoring

## Description

This repository contains projects and tasks related to webstack monitoring, focusing on setting up and managing monitoring tools for web servers. Monitoring is a critical aspect of web development and operations, enabling teams to ensure the health, performance, and availability of their web applications.

## Learning Objectives

By working through the projects in this repository, you will learn:

- The importance of monitoring and how it contributes to the reliability of a webstack.
- How to set up and configure monitoring tools like Datadog.
- How to interpret and utilize monitoring data to maintain a healthy webstack.
- The basics of API interaction for monitoring purposes.
- How to install and configure monitoring agents on web servers.

## Tasks

### 1. Sign Up for Datadog
- Create a free Datadog account using the [US1 region](https://www.datadoghq.com/).
- Set up your account and select relevant statistics from your tech stack to monitor.

### 2. Install Datadog Agent on Web Server
- Install the Datadog agent on your web server (`web-01`).
- Ensure that the agent is correctly configured to monitor the server.
- The server should be visible in the Datadog dashboard under the hostname `XX-web-01`.

### 3. Create API and Application Keys
- Generate an API key and an application key in your Datadog account.
- Copy these keys to your intranet user profile as specified.

### 4. Verify Monitoring Setup
- Use the Datadog API to verify that your server (`web-01`) is being monitored correctly.
- Check that the server appears in the Datadog dashboard with the correct hostname.

## Usage

### Verify Server Monitoring with Datadog API

Use the following `curl` command to verify that your server is being monitored by Datadog:

```bash
curl -X GET "https://api.datadoghq.com/api/v1/hosts?api_key=<YOUR_API_KEY>" -H "Content-Type: application/json"
