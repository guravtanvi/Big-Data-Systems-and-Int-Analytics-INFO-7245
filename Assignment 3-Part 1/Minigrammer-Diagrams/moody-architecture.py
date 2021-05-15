from diagrams import Diagram, Cluster
from diagrams.custom import Custom
from diagrams.onprem.analytics import Spark
from diagrams.onprem.analytics import Hadoop

 
with Diagram("Moody Analytics API Architecture", show=False, filename="moody-architecture", direction="LR"):
   
    api = Custom("API", "./api-icon.png")
    users = Custom("Users", "./users-icon.png")
    firewall = Custom("Firewall", "./firewall-icon.png")
    website = Custom("Website", "./website-icon.png")
    data_service = Custom("Dataservice", "./dataservice-icon.png")
    spark = Spark("Apache Spark")
    hdfs = Hadoop("HDFS")
  
    api >> firewall 
    users >> firewall
    firewall >> website 
    website >> data_service
    data_service >> spark
    spark >> hdfs