# Azure Basics

Azure is Microsoft's cloud computing service, providing a wide range of services including computing, analytics, storage, and networking. Users can pick and choose from these services to develop and scale new applications, or run existing applications, in the public cloud.

### Azure Regions and Availability Zones

-   **Regions** : Azure regions are global data centers where Azure resources are hosted. They ensure that data residency, sovereignty, and compliance requirements are honoured within geographical boundaries.
-   **Availability Zones** : Within each Azure region, there are multiple availability zones. Each zone is made up of one or more data centers equipped with power, cooling, and networking. Availability zones are designed to provide high availability, fault tolerance, and scalability by allowing resources to be distributed across zones within a region.

### How Azure is Structured/Organised

-   **Management Groups** : These are containers that help manage access, policies, and compliance for multiple subscriptions.
-   **Subscriptions** : A subscription is a logical container used to provision resources in Azure. It can help manage costs and resources created by users.
-   **Resource Groups** : Within a subscription, resources can be grouped into resource groups. This is a container that holds related resources for an Azure solution. For example, an application's web app, databases, and storage accounts might be grouped into a single resource group.
-   **Resources** : The smallest units in Azure, representing instances of services that you use, like virtual machines (VMs), SQL databases, etc.

### Categories of Services Azure Provides

-   **Compute** : These services provide virtual machines, containers, and batch processing, as well as supporting remote application access.
-   **Azure DevOps**: CI/CD, etc.
-   **Networking** : This category includes services for connectivity, DNS hosting, network protection against DDoS attacks, and more.
-   **Storage** : Azure offers scalable cloud storage for disk storage for VMs, file storage, and data warehousing services.
-   **Databases** : Managed database services like SQL Database, Cosmos DB, Database for MySQL, and more.
-   **AI and Machine Learning** : Services and tools to build and deploy AI and machine learning models.
-   **IoT** : Services to support Internet of Things applications.
-   **Security & Identity** : Tools and services to secure your applications and manage user authentication and permissions.

### Azure Pricing Calculator

The Azure Pricing Calculator is a tool to help estimate your monthly Azure bill. It's useful for:

-   **Cost Management** : Before deploying any services, you can get an estimate of the costs based on your expected usage.
-   **Budget Planning** : Helps in budgeting for projects by providing cost estimates for the resources required.
-   **Comparison** : Allows you to compare the costs of different configurations and services to find the most cost-effective solution for your needs.
-   **Scenario Testing** : You can estimate the costs for different scenarios, helping in decision-making for scaling, deployment, and resource allocation.

### Diagrams for Azure Regions and Availability Zones

![Azure Regions]()

### Why/When to use the Azure Pricing Calculator

The Azure Pricing Calculator is used to estimate the cost of Azure services before you deploy them. It's useful for budget planning and cost management, allowing you to tailor your Azure resources to your budget and needs. You use it when planning new projects or scaling existing ones to avoid unexpected expenses.
