'''
Auto Scaling:
    - Auto scaling helps you to ensure that you have the correct number of EC2
        instances. 
    - CloudWatch allows you to monitor the usage of your instances. It will not
        modify your EC2 instances though. 
    - Auto scaling allows you to add or take away EC2 instances based on the 
        requirements that you define. 
    - Scaling:  Scaling out and scaling in.  Ex CPU usage of over 80%.
        Terminating instances is scaling in. 
    - How:
        Create launch configuration, then auto scaling group, then auto scaling policy. 
    - Launch Configuration:
        Defining what will be launched when auto scaling kicks in. 
    - Auto Scaling
        Defining where the deployment takes place.  Which VPC and Subnets, Load balancer, 
        Minimum and maximum number of instances. 
    - Policy
        Specifying when to launch the instances. 
    - Ex:  CPU usage > 80% for 5 minutes. Add 2 EC2 instances. Scale down when CPU usage
            < 20% for 5 minutes terminate 1 instance.
            "Let Auto scale manage resources while you're focused on other things"


'''





