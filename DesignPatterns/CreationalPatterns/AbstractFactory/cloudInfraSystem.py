# Abstract Base Classes for Cloud Resources
# These classes define the interface for Compute, Network, and Storage resources
# in the cloud. Each resource type has a set of methods that must be implemented
# by concrete implementations.

from abc import ABC, abstractmethod


class ComputeResource(ABC):
    @abstractmethod
    def launch(self) -> Dict[str, Any]:
        """Launch a compute instance"""
        pass

    @abstractmethod
    def stop(self) -> bool:
        """Stop a compute instance"""
        pass

class NetworkResource(ABC):
    @abstractmethod
    def create_network(self) -> Dict[str, Any]:
        """Create a network configuration"""
        pass

    @abstractmethod
    def configure_firewall(self, rules: List[Dict[str, Any]]) -> bool:
        """Configure network firewall rules"""
        pass

class StorageResource(ABC):
    @abstractmethod
    def create_volume(self, size: int) -> Dict[str, Any]:
        """Create a storage volume"""
        pass

    @abstractmethod
    def attach_volume(self, instance_id: str, volume_id: str) -> bool:
        """Attach a storage volume to an instance"""
        pass

# Abstract Factory for Cloud Provider Infrastructure
# This class defines the interface for creating cloud provider infrastructure
# resources. Each cloud provider must implement this interface to provide its
# own implementation of the resources.

class CloudProviderFactory(ABC):
    @abstractmethod
    def create_compute_resource(self) -> ComputeResource:
        """Create a compute resource for the cloud provider"""
        pass

    @abstractmethod
    def create_network_resource(self) -> NetworkResource:
        """Create a network resource for the cloud provider"""
        pass

    @abstractmethod
    def create_storage_resource(self) -> StorageResource:
        """Create a storage resource for the cloud provider"""
        pass

# Concrete Implementations for AWS
class AWSComputeResource(ComputeResource):
    def __init__(self):
        self.instance_id = None

    def launch(self) -> Dict[str, Any]:
        # Simulate AWS EC2 instance launch
        self.instance_id = f"aws-ec2-{uuid.uuid4()}"
        return {
            "provider": "AWS",
            "instance_id": self.instance_id,
            "type": "t2.micro",
            "status": "running"
        }

    def stop(self) -> bool:
        if self.instance_id:
            # Simulate stopping an AWS instance
            return True
        return False

class AWSNetworkResource(NetworkResource):
    def create_network(self) -> Dict[str, Any]:
        # Simulate AWS VPC creation
        return {
            "provider": "AWS",
            "vpc_id": f"aws-vpc-{uuid.uuid4()}",
            "cidr_block": "10.0.0.0/16",
            "status": "active"
        }

    def configure_firewall(self, rules: List[Dict[str, Any]]) -> bool:
        # Simulate AWS security group configuration
        return True

class AWSStorageResource(StorageResource):
    def create_volume(self, size: int) -> Dict[str, Any]:
        # Simulate AWS EBS volume creation
        return {
            "provider": "AWS",
            "volume_id": f"aws-ebs-{uuid.uuid4()}",
            "size_gb": size,
            "type": "gp2"
        }

    def attach_volume(self, instance_id: str, volume_id: str) -> bool:
        # Simulate volume attachment
        return True

# Concrete Implementations for Azure
class AzureComputeResource(ComputeResource):
    def __init__(self):
        self.instance_id = None

    def launch(self) -> Dict[str, Any]:
        # Simulate Azure VM launch
        self.instance_id = f"azure-vm-{uuid.uuid4()}"
        return {
            "provider": "Azure",
            "instance_id": self.instance_id,
            "type": "Standard_B1s",
            "status": "running"
        }

    def stop(self) -> bool:
        if self.instance_id:
            # Simulate stopping an Azure VM
            return True
        return False

class AzureNetworkResource(NetworkResource):
    def create_network(self) -> Dict[str, Any]:
        # Simulate Azure Virtual Network creation
        return {
            "provider": "Azure",
            "vnet_id": f"azure-vnet-{uuid.uuid4()}",
            "cidr_block": "192.168.0.0/16",
            "status": "active"
        }

    def configure_firewall(self, rules: List[Dict[str, Any]]) -> bool:
        # Simulate Azure Network Security Group configuration
        return True

class AzureStorageResource(StorageResource):
    def create_volume(self, size: int) -> Dict[str, Any]:
        # Simulate Azure Managed Disk creation
        return {
            "provider": "Azure",
            "volume_id": f"azure-disk-{uuid.uuid4()}",
            "size_gb": size,
            "type": "Standard_LRS"
        }

    def attach_volume(self, instance_id: str, volume_id: str) -> bool:
        # Simulate volume attachment
        return True

# Concrete Factories
class AWSCloudProviderFactory(CloudProviderFactory):
    def create_compute_resource(self) -> ComputeResource:
        return AWSComputeResource()

    def create_network_resource(self) -> NetworkResource:
        return AWSNetworkResource()

    def create_storage_resource(self) -> StorageResource:
        return AWSStorageResource()

class AzureCloudProviderFactory(CloudProviderFactory):
    def create_compute_resource(self) -> ComputeResource:
        return AzureComputeResource()

    def create_network_resource(self) -> NetworkResource:
        return AzureNetworkResource()

    def create_storage_resource(self) -> StorageResource:
        return AzureStorageResource()

# Infrastructure Management System
# This class provides a way to manage the provisioning of infrastructure
# resources in the cloud. It takes a cloud provider factory as a parameter
# and provides methods to provision the infrastructure resources.

class CloudInfrastructureManager:
    def __init__(self, factory: CloudProviderFactory):
        self.factory = factory
        self.compute = factory.create_compute_resource()
        self.network = factory.create_network_resource()
        self.storage = factory.create_storage_resource()

    def provision_infrastructure(self, config: Dict[str, Any]):
        """
        Provision complete cloud infrastructure based on configuration
        """
        # Create network
        network_config = self.network.create_network()
        
        # Configure firewall
        firewall_rules = config.get('firewall_rules', [])
        self.network.configure_firewall(firewall_rules)
        
        # Launch compute instance
        compute_instance = self.compute.launch()
        
        # Create and attach storage
        storage_size = config.get('storage_size', 50)
        volume = self.storage.create_volume(storage_size)
        self.storage.attach_volume(
            compute_instance['instance_id'], 
            volume['volume_id']
        )
        
        # Return full infrastructure details
        return {
            "network": network_config,
            "compute": compute_instance,
            "storage": volume
        }

# Example Usage
def main():
    # Provision AWS Infrastructure
    print("Provisioning AWS Infrastructure:")
    aws_factory = AWSCloudProviderFactory()
    aws_manager = CloudInfrastructureManager(aws_factory)
    
    aws_config = {
        "firewall_rules": [
            {"port": 80, "protocol": "TCP", "action": "allow"},
            {"port": 443, "protocol": "TCP", "action": "allow"}
        ],
        "storage_size": 100
    }
    
    aws_infrastructure = aws_manager.provision_infrastructure(aws_config)
    print(json.dumps(aws_infrastructure, indent=2))
    
    print("\nProvisioning Azure Infrastructure:")
    # Provision Azure Infrastructure
    azure_factory = AzureCloudProviderFactory()
    azure_manager = CloudInfrastructureManager(azure_factory)
    
    azure_config = {
        "firewall_rules": [
            {"port": 22, "protocol": "TCP", "action": "allow"},
            {"port": 3389, "protocol": "TCP", "action": "allow"}
        ],
        "storage_size": 200
    }
    
    azure_infrastructure = azure_manager.provision_infrastructure(azure_config)
    print(json.dumps(azure_infrastructure, indent=2))

if __name__ == "__main__":
    main()
