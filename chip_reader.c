/**
 * @file quick_start_example1.c
 * @brief Quick start example that presents how to use libnfc
 */

// To compile this simple example:
// $ gcc -o chip_reader chip_reader.c -lnfc

#include <stdlib.h>
#include <nfc/nfc.h>

static void
print_hex(const uint8_t *pbtData, const size_t szBytes)
{
  size_t  szPos;

  for (szPos = 0; szPos < szBytes; szPos++) {
    printf("%02x  ", pbtData[szPos]);
  }
  printf("\n");
}

int
main(int argc, const char *argv[])
{
  nfc_device *pnd;
  nfc_target nt;

  // Allocate only a pointer to nfc_context
  nfc_context *context;

  // Initialize libnfc and set the nfc_context
  nfc_init(&context);
  if (context == NULL) {
    printf("Unable to init libnfc (malloc)\n");
    exit(EXIT_FAILURE);
  }

  //Added the following variable to point to a device, points to the USB serial port
  //const char device[] = "pn532_uart:/dev/ttyUSB0";
  // Open, using the first available NFC device which can be in order of selection:
  //   - default device specified using environment variable or
  //   - first specified device in libnfc.conf (/etc/nfc) or
  //   - first specified device in device-configuration directory (/etc/nfc/devices.d) or
  //   - first auto-detected (if feature is not disabled in libnfc.conf) device
  //   Originally it was NULL, now its device
  //pnd = nfc_open(context, device); //changed NULL to device in order to point to proper device
  pnd = nfc_open(context, &"pn532_uart:/dev/ttyUSB0"); //changed NULL to device in order to point to proper device
  // If the device can't be initiated...
  if (pnd == NULL) {
    printf("ERROR: %s\n", "Unable to open NFC device.");
    exit(EXIT_FAILURE);
  }

  // Set opened NFC device to initiator mode
  if (nfc_initiator_init(pnd) < 0) {
    nfc_perror(pnd, "nfc_initiator_init");
    exit(EXIT_FAILURE);
  }

  // Poll for a ISO14443A (MIFARE) tag
  const nfc_modulation nmMifare = {
    .nmt = NMT_ISO14443A,
    .nbr = NBR_106,
  };

  //Print the hexidecimal UID
  if (nfc_initiator_select_passive_target(pnd, nmMifare, NULL, 0, &nt) > 0) {
    print_hex(nt.nti.nai.abtUid, nt.nti.nai.szUidLen);
  }

  // Close NFC device
  nfc_close(pnd);
  // Release the context
  nfc_exit(context);
  exit(EXIT_SUCCESS);
}
