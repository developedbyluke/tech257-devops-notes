### Storage Accounts

#### Create a Storage Account

To create a new storage account:

```shell
az storage account create --name <storage_account_name> --resource-group <resource_group_name> --location <location> --sku Standard_LRS
```

-   `--sku` specifies the performance tier (Standard_LRS is standard locally redundant storage).

#### List Storage Accounts

To list all storage accounts in a subscription or a specific resource group:

```shell
az storage account list --resource-group <resource_group_name> --output table
```

Omit `--resource-group` to list storage accounts across the subscription.

#### Show Storage Account Details

To display detailed information about a specific storage account:

```shell
az storage account show --name <storage_account_name> --resource-group <resource_group_name>
```

#### Delete a Storage Account

To delete a specific storage account:

```shell
az storage account delete --name <storage_account_name> --resource-group <resource_group_name> --yes
```

-   `--yes` flag bypasses the confirmation prompt.

#### Update a Storage Account

To update the properties of a storage account (e.g., change SKU):

```shell
az storage account update --name <storage_account_name> --resource-group <resource_group_name> --sku Standard_GRS
```

-   This command changes the storage account to geo-redundant storage.

#### Create a Storage Container

To create a container within a storage account:

```shell
az storage container create --account-name <storage_account_name> --name <container_name> --public-access blob --auth-mode login
```

#### Delete a Storage Container

To delete a container from a storage account:

```shell
az storage container delete --account-name <storage_account_name> --name <container_name> --auth-mode login
```

#### List Storage Containers

To list all containers within a storage account:

```shell
az storage container list --account-name <storage_account_name> --auth-mode login --output table
```

Use `--query "[].{ Name:name }"` to format the output to only show container names.

#### Upload a Blob to a Container

To upload a file as a blob into a specific container:

```shell
az storage blob upload --account-name <storage_account_name> --container-name <container_name> --name <blob_name> --file <path_to_file> --auth-mode login
```

az storage blob upload --account-name tech257lukestorage --container-name images --name image1 --file image1 --auth-mode login

#### Delete a Blob

To delete a blob from a container:

```shell
az storage blob delete --account-name <storage_account_name> --container-name <container_name> --name <blob_name> --auth-mode login
```

#### List Blobs in a Container

To list all blobs within a specific container:

```shell
az storage blob list --account-name <storage_account_name> --container-name <container_name> --output table --auth-mode login
```

#### Download a Blob

To download a blob from a container:

```shell
az storage blob download --account-name <storage_account_name> --container-name <container_name> --name <blob_name> --file <path_to_download> --auth-mode login
```
