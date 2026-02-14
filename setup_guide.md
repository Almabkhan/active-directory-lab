# 🔧 Active Directory Lab Setup Guide

## Prerequisites

- VirtualBox or VMware
- Windows Server ISO (Evaluation copy)
- Windows 10 ISO
- Minimum 16GB RAM (8GB for DC, 4GB for client)

## Option 1: VirtualBox Setup

### Step 1: Create Domain Controller VM

1. Create new VM: Windows Server 2019/2022
2. Allocate: 4GB RAM, 50GB disk
3. Install Windows Server
4. Set static IP: 192.168.1.10/24
5. Install AD DS role
6. Promote to DC (domain: example.local)

### Step 2: Create Client VM

1. Create new VM: Windows 10
2. Allocate: 4GB RAM, 50GB disk
3. Install Windows 10
4. Set DNS to DC IP: 192.168.1.10
5. Join domain: example.local

## Option 2: Automated Lab with Vagrant

```bash
# Install Vagrant and VirtualBox
# Create Vagrantfile
vagrant init
