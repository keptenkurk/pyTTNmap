function Decoder(bytes, port) {
  
  var decoded = {};
  var str = '';
  var length = 0;
  for (var i = 0; i < bytes.length-1; i += 1)
    str += (bytes[i] + ',') ;
    length = i;
  str += bytes[length];

  decoded.raw = bytes;
  decoded.hexstring = str;  
  decoded.latitude = (parseInt(bytes[0] + (bytes[1] << 8) + (bytes[2] << 16 )) / 10000) - 90;
  decoded.latitude = Math.round(decoded.latitude * 1000000) / 1000000;
  decoded.longitude = (parseInt(bytes[3] + (bytes[4] << 8) + (bytes[5] << 16 )) / 10000) - 180;
  decoded.longitude = Math.round(decoded.longitude * 1000000) / 1000000;
  decoded.altitude = (bytes[6] + (bytes[7] << 8) )/ 10;
  decoded.hdop = bytes[8] / 10;


  return decoded;
}