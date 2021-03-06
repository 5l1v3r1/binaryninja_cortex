from binaryninja_cortex.platforms import MCU

class Chip(MCU):
    NAME="SAM3X"
    ROM_OFF=0x00080000 
    RAM_OFF=0x20000000 

    IRQ=MCU.IRQ+ [
        "NVIC_SUPC_IRQ",
        "NVIC_RSTC_IRQ",
        "NVIC_RTC_IRQ",
        "NVIC_RTT_IRQ",
        "NVIC_WDT_IRQ",
        "NVIC_PMC_IRQ",
        "NVIC_EEFC0_IRQ",
        "NVIC_EEFC1_IRQ",
        "NVIC_UART_IRQ",
        "NVIC_SMC_SDRAMC_IRQ",
        "NVIC_SDRAMC_IRQ",
        "NVIC_PIOA_IRQ",
        "NVIC_PIOB_IRQ",
        "NVIC_PIOC_IRQ",
        "NVIC_PIOD_IRQ",
        "NVIC_PIOE_IRQ",
        "NVIC_PIOF_IRQ",
        "NVIC_USART0_IRQ",
        "NVIC_USART1_IRQ",
        "NVIC_USART2_IRQ",
        "NVIC_USART3_IRQ",
        "NVIC_HSMCI_IRQ",
        "NVIC_TWI0_IRQ",
        "NVIC_TWI1_IRQ",
        "NVIC_SPI0_IRQ",
        "NVIC_SPI1_IRQ",
        "NVIC_SSC_IRQ",
        "NVIC_TC0_IRQ",
        "NVIC_TC1_IRQ",
        "NVIC_TC2_IRQ",
        "NVIC_TC3_IRQ",
        "NVIC_TC4_IRQ",
        "NVIC_TC5_IRQ",
        "NVIC_TC6_IRQ",
        "NVIC_TC7_IRQ",
        "NVIC_TC8_IRQ",
        "NVIC_PWM_IRQ",
        "NVIC_ADC_IRQ",
        "NVIC_DACC_IRQ",
        "NVIC_DMAC_IRQ",
        "NVIC_UOTGHS_IRQ",
        "NVIC_TRNG_IRQ",
        "NVIC_EMAC_IRQ",
        "NVIC_CAN0_IRQ",
        "NVIC_CAN1_IRQ",
        ]
