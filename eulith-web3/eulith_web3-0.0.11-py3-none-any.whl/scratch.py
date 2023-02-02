from eulith_web3.binding_generator import ContractBindingGenerator

if __name__ == '__main__':
    sources = ['../../../contracts/src/main/sol/uniswap/interfaces/INonfungiblePositionManager.sol',
               '../../../contracts/src/main/sol/uniswap/interfaces/ISwapRouter.sol']
    b = ContractBindingGenerator(
        sources,
        remappings={'@openzeppelin': '../../../node_modules/@openzeppelin'},
        allow_paths=['../../../contracts/src/main'])
    b.generate("hello")

