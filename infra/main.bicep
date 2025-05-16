// main.waf.bicep
// WAF-aligned deployment using Azure Verified Modules (AVM)
param location string = resourceGroup().location
param environment string = 'dev'
param vnetAddressPrefix string = '10.10.0.0/16'
param appSubnetPrefix string = '10.10.1.0/24'
param servicesSubnetPrefix string = '10.10.2.0/24'
param dataSubnetPrefix string = '10.10.3.0/24'

param keyVaultName string 



// Networking with WAF
module networkingwaf 'modules/networking.bicep' = {
  name: 'networkingWaf'
  params: {
    location: location
    vnetAddressPrefix: vnetAddressPrefix
    appSubnetPrefix: appSubnetPrefix
    servicesSubnetPrefix: servicesSubnetPrefix
    dataSubnetPrefix: dataSubnetPrefix
    environment: environment
  }
}


// Key Vault
module keyvault 'modules/keyvault.bicep' = {
  name: 'keyvaultWaf'
  params: {
    location: location
    avm_waf_aligned: true
    keyVaultName: keyVaultName

  }
}


// Example usage to avoid 'declared but never used' warning
// Pass avmWafAlignedConfig to a module (replace with your actual module call)
// module keyVault 'modules/keyvault.bicep' = {
//   name: 'keyVault'
//   params: {
//     avmWafAlignedConfig: avmWafAlignedConfig
//     avm_waf_aligned: true
//     keyVaultName: 'my-keyvault-waf'
//     location: 'eastus'
//   }
// }
