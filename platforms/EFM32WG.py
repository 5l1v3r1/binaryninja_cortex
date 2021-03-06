from binaryninja_cortex.platforms import MCU

class Chip(MCU):
    NAME="EFM32WG"
    ROM_OFF=0x00000000 
    RAM_OFF=0x20000000 

    IRQ=MCU.IRQ+ [
        "NVIC_DMA_IRQ",
        "NVIC_GPIO_EVEN_IRQ",
        "NVIC_TIMER0_IRQ",
        "NVIC_USART0_RX_IRQ",
        "NVIC_USART0_TX_IRQ",
        "NVIC_USB_IRQ",
        "NVIC_ACMP01_IRQ",
        "NVIC_ADC0_IRQ",
        "NVIC_DAC0_IRQ",
        "NVIC_I2C0_IRQ",
        "NVIC_I2C1_IRQ",
        "NVIC_GPIO_ODD_IRQ",
        "NVIC_TIMER1_IRQ",
        "NVIC_TIMER2_IRQ",
        "NVIC_TIMER3_IRQ",
        "NVIC_USART1_RX_IRQ",
        "NVIC_USART1_TX_IRQ",
        "NVIC_LESENSE_IRQ",
        "NVIC_USART2_RX_IRQ",
        "NVIC_USART2_TX_IRQ",
        "NVIC_UART0_RX_IRQ",
        "NVIC_UART0_TX_IRQ",
        "NVIC_UART1_RX_IRQ",
        "NVIC_UART1_TX_IRQ",
        "NVIC_LEUART0_IRQ",
        "NVIC_LEUART1_IRQ",
        "NVIC_LETIMER0_IRQ",
        "NVIC_PCNT0_IRQ",
        "NVIC_PCNT1_IRQ",
        "NVIC_PCNT2_IRQ",
        "NVIC_RTC_IRQ",
        "NVIC_BURTC_IRQ",
        "NVIC_CMU_IRQ",
        "NVIC_VCMP_IRQ",
        "NVIC_LCD_IRQ",
        "NVIC_MSC_IRQ",
        "NVIC_AES_IRQ",
        "NVIC_EBI_IRQ",
        "NVIC_EMU_IRQ",
        ]
