#
# Autogenerated by Thrift Compiler (0.8.0)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py:utf8strings
#

from thrift.Thrift import TType, TMessageType, TException
import elephantdb.ElephantDBShared
from ttypes import *
from thrift.Thrift import TProcessor
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None


class Iface(elephantdb.ElephantDBShared.Iface):
  def get(self, domain, key):
    """
    Parameters:
     - domain
     - key
    """
    pass

  def multiGet(self, domain, key):
    """
    Parameters:
     - domain
     - key
    """
    pass

  def directMultiGet(self, domain, key):
    """
    Parameters:
     - domain
     - key
    """
    pass


class Client(elephantdb.ElephantDBShared.Client, Iface):
  def __init__(self, iprot, oprot=None):
    elephantdb.ElephantDBShared.Client.__init__(self, iprot, oprot)

  def get(self, domain, key):
    """
    Parameters:
     - domain
     - key
    """
    self.send_get(domain, key)
    return self.recv_get()

  def send_get(self, domain, key):
    self._oprot.writeMessageBegin('get', TMessageType.CALL, self._seqid)
    args = get_args()
    args.domain = domain
    args.key = key
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_get(self, ):
    (fname, mtype, rseqid) = self._iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(self._iprot)
      self._iprot.readMessageEnd()
      raise x
    result = get_result()
    result.read(self._iprot)
    self._iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    if result.dnfe is not None:
      raise result.dnfe
    if result.hde is not None:
      raise result.hde
    if result.dnle is not None:
      raise result.dnle
    raise TApplicationException(TApplicationException.MISSING_RESULT, "get failed: unknown result");

  def multiGet(self, domain, key):
    """
    Parameters:
     - domain
     - key
    """
    self.send_multiGet(domain, key)
    return self.recv_multiGet()

  def send_multiGet(self, domain, key):
    self._oprot.writeMessageBegin('multiGet', TMessageType.CALL, self._seqid)
    args = multiGet_args()
    args.domain = domain
    args.key = key
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_multiGet(self, ):
    (fname, mtype, rseqid) = self._iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(self._iprot)
      self._iprot.readMessageEnd()
      raise x
    result = multiGet_result()
    result.read(self._iprot)
    self._iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    if result.dnfe is not None:
      raise result.dnfe
    if result.hde is not None:
      raise result.hde
    if result.dnle is not None:
      raise result.dnle
    raise TApplicationException(TApplicationException.MISSING_RESULT, "multiGet failed: unknown result");

  def directMultiGet(self, domain, key):
    """
    Parameters:
     - domain
     - key
    """
    self.send_directMultiGet(domain, key)
    return self.recv_directMultiGet()

  def send_directMultiGet(self, domain, key):
    self._oprot.writeMessageBegin('directMultiGet', TMessageType.CALL, self._seqid)
    args = directMultiGet_args()
    args.domain = domain
    args.key = key
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_directMultiGet(self, ):
    (fname, mtype, rseqid) = self._iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(self._iprot)
      self._iprot.readMessageEnd()
      raise x
    result = directMultiGet_result()
    result.read(self._iprot)
    self._iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    if result.dnfe is not None:
      raise result.dnfe
    if result.hde is not None:
      raise result.hde
    if result.dnle is not None:
      raise result.dnle
    raise TApplicationException(TApplicationException.MISSING_RESULT, "directMultiGet failed: unknown result");


class Processor(elephantdb.ElephantDBShared.Processor, Iface, TProcessor):
  def __init__(self, handler):
    elephantdb.ElephantDBShared.Processor.__init__(self, handler)
    self._processMap["get"] = Processor.process_get
    self._processMap["multiGet"] = Processor.process_multiGet
    self._processMap["directMultiGet"] = Processor.process_directMultiGet

  def process(self, iprot, oprot):
    (name, type, seqid) = iprot.readMessageBegin()
    if name not in self._processMap:
      iprot.skip(TType.STRUCT)
      iprot.readMessageEnd()
      x = TApplicationException(TApplicationException.UNKNOWN_METHOD, 'Unknown function %s' % (name))
      oprot.writeMessageBegin(name, TMessageType.EXCEPTION, seqid)
      x.write(oprot)
      oprot.writeMessageEnd()
      oprot.trans.flush()
      return
    else:
      self._processMap[name](self, seqid, iprot, oprot)
    return True

  def process_get(self, seqid, iprot, oprot):
    args = get_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = get_result()
    try:
      result.success = self._handler.get(args.domain, args.key)
    except elephantdb.ttypes.DomainNotFoundException, dnfe:
      result.dnfe = dnfe
    except elephantdb.ttypes.HostsDownException, hde:
      result.hde = hde
    except elephantdb.ttypes.DomainNotLoadedException, dnle:
      result.dnle = dnle
    oprot.writeMessageBegin("get", TMessageType.REPLY, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()

  def process_multiGet(self, seqid, iprot, oprot):
    args = multiGet_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = multiGet_result()
    try:
      result.success = self._handler.multiGet(args.domain, args.key)
    except elephantdb.ttypes.DomainNotFoundException, dnfe:
      result.dnfe = dnfe
    except elephantdb.ttypes.HostsDownException, hde:
      result.hde = hde
    except elephantdb.ttypes.DomainNotLoadedException, dnle:
      result.dnle = dnle
    oprot.writeMessageBegin("multiGet", TMessageType.REPLY, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()

  def process_directMultiGet(self, seqid, iprot, oprot):
    args = directMultiGet_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = directMultiGet_result()
    try:
      result.success = self._handler.directMultiGet(args.domain, args.key)
    except elephantdb.ttypes.DomainNotFoundException, dnfe:
      result.dnfe = dnfe
    except elephantdb.ttypes.HostsDownException, hde:
      result.hde = hde
    except elephantdb.ttypes.DomainNotLoadedException, dnle:
      result.dnle = dnle
    oprot.writeMessageBegin("directMultiGet", TMessageType.REPLY, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()


# HELPER FUNCTIONS AND STRUCTURES

class get_args:
  """
  Attributes:
   - domain
   - key
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'domain', None, None, ), # 1
    (2, TType.STRING, 'key', None, None, ), # 2
  )

  def __init__(self, domain=None, key=None,):
    self.domain = domain
    self.key = key

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.domain = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.key = iprot.readString();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('get_args')
    if self.domain is not None:
      oprot.writeFieldBegin('domain', TType.STRING, 1)
      oprot.writeString(self.domain.encode('utf-8'))
      oprot.writeFieldEnd()
    if self.key is not None:
      oprot.writeFieldBegin('key', TType.STRING, 2)
      oprot.writeString(self.key)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class get_result:
  """
  Attributes:
   - success
   - dnfe
   - hde
   - dnle
  """

  thrift_spec = (
    (0, TType.STRUCT, 'success', (elephantdb.ttypes.Value, elephantdb.ttypes.Value.thrift_spec), None, ), # 0
    (1, TType.STRUCT, 'dnfe', (elephantdb.ttypes.DomainNotFoundException, elephantdb.ttypes.DomainNotFoundException.thrift_spec), None, ), # 1
    (2, TType.STRUCT, 'hde', (elephantdb.ttypes.HostsDownException, elephantdb.ttypes.HostsDownException.thrift_spec), None, ), # 2
    (3, TType.STRUCT, 'dnle', (elephantdb.ttypes.DomainNotLoadedException, elephantdb.ttypes.DomainNotLoadedException.thrift_spec), None, ), # 3
  )

  def __init__(self, success=None, dnfe=None, hde=None, dnle=None,):
    self.success = success
    self.dnfe = dnfe
    self.hde = hde
    self.dnle = dnle

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 0:
        if ftype == TType.STRUCT:
          self.success = elephantdb.ttypes.Value()
          self.success.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 1:
        if ftype == TType.STRUCT:
          self.dnfe = elephantdb.ttypes.DomainNotFoundException()
          self.dnfe.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRUCT:
          self.hde = elephantdb.ttypes.HostsDownException()
          self.hde.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRUCT:
          self.dnle = elephantdb.ttypes.DomainNotLoadedException()
          self.dnle.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('get_result')
    if self.success is not None:
      oprot.writeFieldBegin('success', TType.STRUCT, 0)
      self.success.write(oprot)
      oprot.writeFieldEnd()
    if self.dnfe is not None:
      oprot.writeFieldBegin('dnfe', TType.STRUCT, 1)
      self.dnfe.write(oprot)
      oprot.writeFieldEnd()
    if self.hde is not None:
      oprot.writeFieldBegin('hde', TType.STRUCT, 2)
      self.hde.write(oprot)
      oprot.writeFieldEnd()
    if self.dnle is not None:
      oprot.writeFieldBegin('dnle', TType.STRUCT, 3)
      self.dnle.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class multiGet_args:
  """
  Attributes:
   - domain
   - key
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'domain', None, None, ), # 1
    (2, TType.SET, 'key', (TType.STRING,None), None, ), # 2
  )

  def __init__(self, domain=None, key=None,):
    self.domain = domain
    self.key = key

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.domain = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.SET:
          self.key = set()
          (_etype3, _size0) = iprot.readSetBegin()
          for _i4 in xrange(_size0):
            _elem5 = iprot.readString();
            self.key.add(_elem5)
          iprot.readSetEnd()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('multiGet_args')
    if self.domain is not None:
      oprot.writeFieldBegin('domain', TType.STRING, 1)
      oprot.writeString(self.domain.encode('utf-8'))
      oprot.writeFieldEnd()
    if self.key is not None:
      oprot.writeFieldBegin('key', TType.SET, 2)
      oprot.writeSetBegin(TType.STRING, len(self.key))
      for iter6 in self.key:
        oprot.writeString(iter6)
      oprot.writeSetEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class multiGet_result:
  """
  Attributes:
   - success
   - dnfe
   - hde
   - dnle
  """

  thrift_spec = (
    (0, TType.MAP, 'success', (TType.STRING,None,TType.STRUCT,(elephantdb.ttypes.Value, elephantdb.ttypes.Value.thrift_spec)), None, ), # 0
    (1, TType.STRUCT, 'dnfe', (elephantdb.ttypes.DomainNotFoundException, elephantdb.ttypes.DomainNotFoundException.thrift_spec), None, ), # 1
    (2, TType.STRUCT, 'hde', (elephantdb.ttypes.HostsDownException, elephantdb.ttypes.HostsDownException.thrift_spec), None, ), # 2
    (3, TType.STRUCT, 'dnle', (elephantdb.ttypes.DomainNotLoadedException, elephantdb.ttypes.DomainNotLoadedException.thrift_spec), None, ), # 3
  )

  def __init__(self, success=None, dnfe=None, hde=None, dnle=None,):
    self.success = success
    self.dnfe = dnfe
    self.hde = hde
    self.dnle = dnle

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 0:
        if ftype == TType.MAP:
          self.success = {}
          (_ktype8, _vtype9, _size7 ) = iprot.readMapBegin() 
          for _i11 in xrange(_size7):
            _key12 = iprot.readString();
            _val13 = elephantdb.ttypes.Value()
            _val13.read(iprot)
            self.success[_key12] = _val13
          iprot.readMapEnd()
        else:
          iprot.skip(ftype)
      elif fid == 1:
        if ftype == TType.STRUCT:
          self.dnfe = elephantdb.ttypes.DomainNotFoundException()
          self.dnfe.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRUCT:
          self.hde = elephantdb.ttypes.HostsDownException()
          self.hde.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRUCT:
          self.dnle = elephantdb.ttypes.DomainNotLoadedException()
          self.dnle.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('multiGet_result')
    if self.success is not None:
      oprot.writeFieldBegin('success', TType.MAP, 0)
      oprot.writeMapBegin(TType.STRING, TType.STRUCT, len(self.success))
      for kiter14,viter15 in self.success.items():
        oprot.writeString(kiter14)
        viter15.write(oprot)
      oprot.writeMapEnd()
      oprot.writeFieldEnd()
    if self.dnfe is not None:
      oprot.writeFieldBegin('dnfe', TType.STRUCT, 1)
      self.dnfe.write(oprot)
      oprot.writeFieldEnd()
    if self.hde is not None:
      oprot.writeFieldBegin('hde', TType.STRUCT, 2)
      self.hde.write(oprot)
      oprot.writeFieldEnd()
    if self.dnle is not None:
      oprot.writeFieldBegin('dnle', TType.STRUCT, 3)
      self.dnle.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class directMultiGet_args:
  """
  Attributes:
   - domain
   - key
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'domain', None, None, ), # 1
    (2, TType.SET, 'key', (TType.STRING,None), None, ), # 2
  )

  def __init__(self, domain=None, key=None,):
    self.domain = domain
    self.key = key

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.domain = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.SET:
          self.key = set()
          (_etype19, _size16) = iprot.readSetBegin()
          for _i20 in xrange(_size16):
            _elem21 = iprot.readString();
            self.key.add(_elem21)
          iprot.readSetEnd()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('directMultiGet_args')
    if self.domain is not None:
      oprot.writeFieldBegin('domain', TType.STRING, 1)
      oprot.writeString(self.domain.encode('utf-8'))
      oprot.writeFieldEnd()
    if self.key is not None:
      oprot.writeFieldBegin('key', TType.SET, 2)
      oprot.writeSetBegin(TType.STRING, len(self.key))
      for iter22 in self.key:
        oprot.writeString(iter22)
      oprot.writeSetEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class directMultiGet_result:
  """
  Attributes:
   - success
   - dnfe
   - hde
   - dnle
  """

  thrift_spec = (
    (0, TType.MAP, 'success', (TType.STRING,None,TType.STRUCT,(elephantdb.ttypes.Value, elephantdb.ttypes.Value.thrift_spec)), None, ), # 0
    (1, TType.STRUCT, 'dnfe', (elephantdb.ttypes.DomainNotFoundException, elephantdb.ttypes.DomainNotFoundException.thrift_spec), None, ), # 1
    (2, TType.STRUCT, 'hde', (elephantdb.ttypes.HostsDownException, elephantdb.ttypes.HostsDownException.thrift_spec), None, ), # 2
    (3, TType.STRUCT, 'dnle', (elephantdb.ttypes.DomainNotLoadedException, elephantdb.ttypes.DomainNotLoadedException.thrift_spec), None, ), # 3
  )

  def __init__(self, success=None, dnfe=None, hde=None, dnle=None,):
    self.success = success
    self.dnfe = dnfe
    self.hde = hde
    self.dnle = dnle

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 0:
        if ftype == TType.MAP:
          self.success = {}
          (_ktype24, _vtype25, _size23 ) = iprot.readMapBegin() 
          for _i27 in xrange(_size23):
            _key28 = iprot.readString();
            _val29 = elephantdb.ttypes.Value()
            _val29.read(iprot)
            self.success[_key28] = _val29
          iprot.readMapEnd()
        else:
          iprot.skip(ftype)
      elif fid == 1:
        if ftype == TType.STRUCT:
          self.dnfe = elephantdb.ttypes.DomainNotFoundException()
          self.dnfe.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRUCT:
          self.hde = elephantdb.ttypes.HostsDownException()
          self.hde.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRUCT:
          self.dnle = elephantdb.ttypes.DomainNotLoadedException()
          self.dnle.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('directMultiGet_result')
    if self.success is not None:
      oprot.writeFieldBegin('success', TType.MAP, 0)
      oprot.writeMapBegin(TType.STRING, TType.STRUCT, len(self.success))
      for kiter30,viter31 in self.success.items():
        oprot.writeString(kiter30)
        viter31.write(oprot)
      oprot.writeMapEnd()
      oprot.writeFieldEnd()
    if self.dnfe is not None:
      oprot.writeFieldBegin('dnfe', TType.STRUCT, 1)
      self.dnfe.write(oprot)
      oprot.writeFieldEnd()
    if self.hde is not None:
      oprot.writeFieldBegin('hde', TType.STRUCT, 2)
      self.hde.write(oprot)
      oprot.writeFieldEnd()
    if self.dnle is not None:
      oprot.writeFieldBegin('dnle', TType.STRUCT, 3)
      self.dnle.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)
