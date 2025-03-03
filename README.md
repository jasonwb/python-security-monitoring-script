#security-monitoring-scripts

Simple Ansible playbook that deploys a security monitoring script across multiple servers. It does the following:

1.  Copies a Python-based network monitoring script to target servers
2.  Ensures necessary dependencies are installed (e.g., tcpdump, python3)
3.  Sets up a cron job to run the script periodically
