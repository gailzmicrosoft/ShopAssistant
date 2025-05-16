// modules/networking.bicep
param location string
param vnetAddressPrefix string // example value: '10.10.0.0/16'
param appSubnetPrefix string
param servicesSubnetPrefix string
param dataSubnetPrefix string
param environment string

resource vnet 'Microsoft.Network/virtualNetworks@2023-04-01' = {
  name: 'vnet-${environment}'
  location: location
  properties: {
    addressSpace: {
      addressPrefixes: [vnetAddressPrefix]
    }
    subnets: [
      {
        name: 'app'
        properties: {
          addressPrefix: appSubnetPrefix
          networkSecurityGroup: {
            id: appNsg.id
          }
          routeTable: {
            id: routeTable.id
          }
        }
      }
      {
        name: 'services'
        properties: {
          addressPrefix: servicesSubnetPrefix
          networkSecurityGroup: {
            id: servicesNsg.id
          }
        }
      }
      {
        name: 'data'
        properties: {
          addressPrefix: dataSubnetPrefix
          networkSecurityGroup: {
            id: dataNsg.id
          }
        }
      }
    ]
  }
}

// NSGs for each subnet
resource appNsg 'Microsoft.Network/networkSecurityGroups@2023-04-01' = {
  name: 'nsg-app-${environment}'
  location: location
}
resource servicesNsg 'Microsoft.Network/networkSecurityGroups@2023-04-01' = {
  name: 'nsg-services-${environment}'
  location: location
}
resource dataNsg 'Microsoft.Network/networkSecurityGroups@2023-04-01' = {
  name: 'nsg-data-${environment}'
  location: location
}

// Route Table (example, can be extended)
resource routeTable 'Microsoft.Network/routeTables@2023-04-01' = {
  name: 'rt-${environment}'
  location: location
}

// Bastion Host (requires dedicated subnet and public IP)
resource bastionSubnet 'Microsoft.Network/virtualNetworks/subnets@2023-04-01' = {
  parent: vnet
  name: 'AzureBastionSubnet'
  properties: {
    addressPrefix: '10.10.10.0/27'
  }
}
resource bastionPublicIp 'Microsoft.Network/publicIPAddresses@2023-04-01' = {
  name: 'bastion-pip-${environment}'
  location: location
  sku: {
    name: 'Standard'
  }
  properties: {
    publicIPAllocationMethod: 'Static'
  }
}
resource bastionHost 'Microsoft.Network/bastionHosts@2023-04-01' = {
  name: 'bastion-${environment}'
  location: location
  properties: {
    ipConfigurations: [
      {
        name: 'bastion-ip-config'
        properties: {
          subnet: {
            id: bastionSubnet.id
          }
          publicIPAddress: {
            id: bastionPublicIp.id
          }
        }
      }
    ]
  }
}

// Private DNS Zone (example for privatelink.vaultcore.azure.net)
resource privateDnsZone 'Microsoft.Network/privateDnsZones@2023-05-01' = {
  name: 'privatelink.vaultcore.azure.net'
  location: location
}

output vnetId string = vnet.id
output appSubnetId string = vnet.properties.subnets[0].id
output servicesSubnetId string = vnet.properties.subnets[1].id
output dataSubnetId string = vnet.properties.subnets[2].id
output appNsgId string = appNsg.id
output servicesNsgId string = servicesNsg.id
output dataNsgId string = dataNsg.id
output routeTableId string = routeTable.id
output bastionHostId string = bastionHost.id
output bastionPublicIpId string = bastionPublicIp.id
output privateDnsZoneId string = privateDnsZone.id
