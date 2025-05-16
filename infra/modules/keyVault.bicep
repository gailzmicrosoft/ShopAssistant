// modules/keyvault.bicep
@description('Indicates whether AVM WAF is aligned.')
param avm_waf_aligned bool
@description('Key Vault name.')
param keyVaultName string
@description('Azure location for Key Vault.')
param location string
@description('Resource ID of the data subnet for private endpoint (required if avm_waf_aligned is true).')
param dataSubnetId string = ''

module keyVault 'br/public:avm/res/key-vault/vault:0.12.1' = {
  name: 'keyVault-${keyVaultName}'
  params: {
    name: keyVaultName
    enablePurgeProtection: true
    enableRbacAuthorization: false
    softDeleteRetentionInDays: 7
    tags: {
      Environment: 'Non-Prod'
      'hidden-title': 'This is visible in the resource name'
      Role: 'DeploymentValidation'
    }
  }
}

resource keyVaultPrivateEndpoint 'Microsoft.Network/privateEndpoints@2023-05-01' = if (avm_waf_aligned) {
  name: 'kv-pe-${keyVaultName}'
  location: location
  properties: {
    subnet: {
      id: dataSubnetId
    }
    privateLinkServiceConnections: [
      {
        name: 'keyvault-connection'
        properties: {
          privateLinkServiceId: keyVault.outputs.resourceId
          groupIds: [ 'vault' ]
        }
      }
    ]
  }
}

