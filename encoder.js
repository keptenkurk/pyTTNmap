function Encoder(object, port) {
  // Encode downlink messages sent as
  // object to an array or buffer of bytes.
  // Encode packets (2 byte), gateways (1 byte), distance (2 byte)
  // in big endian (MSB first)
  var bytes = [];
  if (port == 1){
  bytes[0] = object.packets >> 8;
  bytes[1] = object.packets - ( 256 * bytes[0]);
  bytes[2] = object.gateways;
  bytes[3] = object.distance >> 8;
  bytes[4] = object.distance - ( 256 * bytes[3]);
  }
  return bytes;
}