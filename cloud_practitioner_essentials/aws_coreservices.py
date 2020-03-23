'''
AWS Core Services 
    Elastic Cloud (EC2):
    - Standands for Elastic Compute Cloud.  Compute refers to servers. 
        Cloud refers to they are in the cloud.  Elastic refers to the 
        fact that in you can increase or decrease resources. 
    - Instances:
        Are pay as you go.  Only pay for one that you use and when they
        are running. 
    - Build & Configure EC2 Instances:
        Login, choose region, launch EC2 wizard, select AMI, select 
        instance type (hardware), configure network, storage and key-pairs. 
    - AMI
        refers to amazon machine image.  Refers to the software that will
        be used to launch the server.  
    - Hardware - Called instance type
        t2.micro is the low end. 
    - Configure instance details. 
        Network: use default. 
    - Add storage:
        By gigs, change type of disck. 
        Can add additional volumes. 
        Can delete when terminate EC2. 
    - Give tag 
        Its a name for your instance. 
    - Security Group
        set of firewall rules.  SSH connectivity. 
        Give it a name. 
    - Luanch    
        review selections and launch. 
    - Key Pair
        need to create before lauching.
        download the private key. 
        required to connect over ssh. 
    - Connection
        Copy and past DNS  username@dns



Elastick Block Store
    - EBS volumes are the storage types for your instance. 
    - Designed to be durable and available. Replicated across multiple
      servers. 
    - Block level replication:  can separate instances for data and os to run
      faster. 
    - Snapshots:  can create snapshots of your instances.  
    - Encryption: at no additional cost to encrypt data between transit 
      between server instances. 
    - Can create new volumes and transfer them without stopping the instance. 

    Process:
        - Go to EC2 Instances
        - Go to Elastic Block Store > volumes
        - New volume needs to be created in the same availability zone. 
        - Select volume type. 
        - Choose size. 
        - Click create volume. Gives you a volume ID. 
        - Attached to EC2 instance: go to actions, attach volume, choose
          the device name and attached.  
        - If you type lsblk you can see the block storage devices that are
          attached to the EC2 instance.  You can create a file system 
          in this block. Then you can create a folder in your linux system 
          that saves data to that other block instance. 
          So you mount the volume to the EC2 instance. 
        - Also can detach volume from the instance and attach to another
          available EC2 instance.  
        - Tags:  you can use tags to group and vizualize billing by type. 


    Amazon S3 - Simple Storage Service
        - Provides a simple api to store data. 
        - Not saved in any one server. 
        - Can be almost any data file. Can be as large as terrabytes in size. 
        - Low latency access.
        - User defines security measures, access controls, etc. 
        - When saving an object, you need to create a key that is like a file path. 
        - Only be billed for what you use. 
        - Can access via the managemet console, CLI or SKD. 
        - You can also use a URL.  Need bucket name, region end point, and object key. 
        - Snowball?
    
    Global Infrastructure
        - Regions:  geographic areas that host 2 or more availability zones. 
                    Objective should be to optomize latency, cost and compliance. 
                    regions are completely separate entities.  data is not replicated
                    between regions. 
        - availability zones: collection of data centers in a specific region. they are 
                    physically isolated, but network connected.  they have their own 
                    power and network connectivity. 
                    This means that they are protected from failures in other zones. 
        - edge locations:  amazon cloud front.  used to deliver content to your customers. 
                    customers have access to quicker content.  

    Amazon Virtual Private Cloud (VPC)
        - pay as you go on demand compute as well as compute resources. 
        - VPC is the network service.  it allows you to create a private network within 
            the aws cloud.  it is easier to set up via amazon than a local solution. 
            It is an aws foundational services and integrates with the other services. 
            Ex: an EC2 or database instances get deployed into your VPC.  
        - Amazon VPC's live within regions and you can have multiple VPC's by region. 
            Subnets are smaller sub control areas within the vpc. 
        - Subnet: sounds like you need to assign ip addresses per subnet. You define which              Availability zone it exists. 
    
    Security Groups
        - Act as a built-in firewall. 
        - You have full control over accessibility. 
        - Filter traffic to your instances. 
        - Ex:  database tier that can only accept requests from the applicaton tier, 
            same with a web instance. 
        - Good security groups necessary for security compliance. 
        - 

'''




