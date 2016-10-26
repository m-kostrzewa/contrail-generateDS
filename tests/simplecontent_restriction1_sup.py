#!/usr/bin/env python
# -*- coding: utf-8 -*- 

#
# Generated  by generateDS.py.
#

import sys
import getopt
import re as re_

etree_ = None
Verbose_import_ = False
(   XMLParser_import_none, XMLParser_import_lxml,
    XMLParser_import_elementtree
    ) = range(3)
XMLParser_import_library = None
try:
    # lxml
    from lxml import etree as etree_
    XMLParser_import_library = XMLParser_import_lxml
    if Verbose_import_:
        print("running with lxml.etree")
except ImportError:
    try:
        # cElementTree from Python 2.5+
        import xml.etree.cElementTree as etree_
        XMLParser_import_library = XMLParser_import_elementtree
        if Verbose_import_:
            print("running with cElementTree on Python 2.5+")
    except ImportError:
        try:
            # ElementTree from Python 2.5+
            import xml.etree.ElementTree as etree_
            XMLParser_import_library = XMLParser_import_elementtree
            if Verbose_import_:
                print("running with ElementTree on Python 2.5+")
        except ImportError:
            try:
                # normal cElementTree install
                import cElementTree as etree_
                XMLParser_import_library = XMLParser_import_elementtree
                if Verbose_import_:
                    print("running with cElementTree")
            except ImportError:
                try:
                    # normal ElementTree install
                    import elementtree.ElementTree as etree_
                    XMLParser_import_library = XMLParser_import_elementtree
                    if Verbose_import_:
                        print("running with ElementTree")
                except ImportError:
                    raise ImportError("Failed to import ElementTree from any known place")

def parsexml_(*args, **kwargs):
    if (XMLParser_import_library == XMLParser_import_lxml and
        'parser' not in kwargs):
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        kwargs['parser'] = etree_.ETCompatXMLParser()
    doc = etree_.parse(*args, **kwargs)
    return doc

#
# User methods
#
# Calls to the methods in these classes are generated by generateDS.py.
# You can replace these methods by re-implementing the following class
#   in a module named generatedssuper.py.

try:
    from generatedssuper import GeneratedsSuper
except ImportError, exp:

    class GeneratedsSuper(object):
        def gds_format_string(self, input_data, input_name=''):
            return input_data
        def gds_validate_string(self, input_data, node, input_name=''):
            return input_data
        def gds_format_integer(self, input_data, input_name=''):
            return '%d' % input_data
        def gds_validate_integer(self, input_data, node, input_name=''):
            return input_data
        def gds_format_integer_list(self, input_data, input_name=''):
            return '%s' % input_data
        def gds_validate_integer_list(self, input_data, node, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    fvalue = float(value)
                except (TypeError, ValueError), exp:
                    raise_parse_error(node, 'Requires sequence of integers')
            return input_data
        def gds_format_float(self, input_data, input_name=''):
            return '%f' % input_data
        def gds_validate_float(self, input_data, node, input_name=''):
            return input_data
        def gds_format_float_list(self, input_data, input_name=''):
            return '%s' % input_data
        def gds_validate_float_list(self, input_data, node, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    fvalue = float(value)
                except (TypeError, ValueError), exp:
                    raise_parse_error(node, 'Requires sequence of floats')
            return input_data
        def gds_format_double(self, input_data, input_name=''):
            return '%e' % input_data
        def gds_validate_double(self, input_data, node, input_name=''):
            return input_data
        def gds_format_double_list(self, input_data, input_name=''):
            return '%s' % input_data
        def gds_validate_double_list(self, input_data, node, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    fvalue = float(value)
                except (TypeError, ValueError), exp:
                    raise_parse_error(node, 'Requires sequence of doubles')
            return input_data
        def gds_format_boolean(self, input_data, input_name=''):
            return '%s' % input_data
        def gds_validate_boolean(self, input_data, node, input_name=''):
            return input_data
        def gds_format_boolean_list(self, input_data, input_name=''):
            return '%s' % input_data
        def gds_validate_boolean_list(self, input_data, node, input_name=''):
            values = input_data.split()
            for value in values:
                if value not in ('true', '1', 'false', '0', ):
                    raise_parse_error(node, 'Requires sequence of booleans ("true", "1", "false", "0")')
            return input_data
        def gds_str_lower(self, instring):
            return instring.lower()
        def get_path_(self, node):
            path_list = []
            self.get_path_list_(node, path_list)
            path_list.reverse()
            path = '/'.join(path_list)
            return path
        Tag_strip_pattern_ = re_.compile(r'\{.*\}')
        def get_path_list_(self, node, path_list):
            if node is None:
                return
            tag = GeneratedsSuper.Tag_strip_pattern_.sub('', node.tag)
            if tag:
                path_list.append(tag)
            self.get_path_list_(node.getparent(), path_list)
        def get_class_obj_(self, node, default_class=None):
            class_obj1 = default_class
            if 'xsi' in node.nsmap:
                classname = node.get('{%s}type' % node.nsmap['xsi'])
                if classname is not None:
                    names = classname.split(':')
                    if len(names) == 2:
                        classname = names[1]
                    class_obj2 = globals().get(classname)
                    if class_obj2 is not None:
                        class_obj1 = class_obj2
            return class_obj1
        def gds_build_any(self, node, type_name=None):
            return None


#
# If you have installed IPython you can uncomment and use the following.
# IPython is available from http://ipython.scipy.org/.
#

## from IPython.Shell import IPShellEmbed
## args = ''
## ipshell = IPShellEmbed(args,
##     banner = 'Dropping into IPython',
##     exit_msg = 'Leaving Interpreter, back to program.')

# Then use the following line where and when you want to drop into the
# IPython shell:
#    ipshell('<some message> -- Entering ipshell.\nHit Ctrl-D to exit')

#
# Globals
#

ExternalEncoding = 'ascii'
Tag_pattern_ = re_.compile(r'({.*})?(.*)')
String_cleanup_pat_ = re_.compile(r"[\n\r\s]+")
Namespace_extract_pat_ = re_.compile(r'{(.*)}(.*)')

#
# Support/utility functions.
#

def showIndent(outfile, level, pretty_print=True):
    if pretty_print:
        for idx in range(level):
            outfile.write('    ')

def quote_xml(inStr):
    if not inStr:
        return ''
    s1 = (isinstance(inStr, basestring) and inStr or
          '%s' % inStr)
    s1 = s1.replace('&', '&amp;')
    s1 = s1.replace('<', '&lt;')
    s1 = s1.replace('>', '&gt;')
    return s1

def quote_attrib(inStr):
    s1 = (isinstance(inStr, basestring) and inStr or
          '%s' % inStr)
    s1 = s1.replace('&', '&amp;')
    s1 = s1.replace('<', '&lt;')
    s1 = s1.replace('>', '&gt;')
    if '"' in s1:
        if "'" in s1:
            s1 = '"%s"' % s1.replace('"', "&quot;")
        else:
            s1 = "'%s'" % s1
    else:
        s1 = '"%s"' % s1
    return s1

def quote_python(inStr):
    s1 = inStr
    if s1.find("'") == -1:
        if s1.find('\n') == -1:
            return "'%s'" % s1
        else:
            return "'''%s'''" % s1
    else:
        if s1.find('"') != -1:
            s1 = s1.replace('"', '\\"')
        if s1.find('\n') == -1:
            return '"%s"' % s1
        else:
            return '"""%s"""' % s1

def get_all_text_(node):
    if node.text is not None:
        text = node.text
    else:
        text = ''
    for child in node:
        if child.tail is not None:
            text += child.tail
    return text

def find_attr_value_(attr_name, node):
    attrs = node.attrib
    attr_parts = attr_name.split(':')
    value = None
    if len(attr_parts) == 1:
        value = attrs.get(attr_name)
    elif len(attr_parts) == 2:
        prefix, name = attr_parts
        namespace = node.nsmap.get(prefix)
        if namespace is not None:
            value = attrs.get('{%s}%s' % (namespace, name, ))
    return value


class GDSParseError(Exception):
    pass

def raise_parse_error(node, msg):
    if XMLParser_import_library == XMLParser_import_lxml:
        msg = '%s (element %s/line %d)' % (msg, node.tag, node.sourceline, )
    else:
        msg = '%s (element %s)' % (msg, node.tag, )
    raise GDSParseError(msg)


class MixedContainer:
    # Constants for category:
    CategoryNone = 0
    CategoryText = 1
    CategorySimple = 2
    CategoryComplex = 3
    # Constants for content_type:
    TypeNone = 0
    TypeText = 1
    TypeString = 2
    TypeInteger = 3
    TypeFloat = 4
    TypeDecimal = 5
    TypeDouble = 6
    TypeBoolean = 7
    def __init__(self, category, content_type, name, value):
        self.category = category
        self.content_type = content_type
        self.name = name
        self.value = value
    def getCategory(self):
        return self.category
    def getContenttype(self, content_type):
        return self.content_type
    def getValue(self):
        return self.value
    def getName(self):
        return self.name
    def export(self, outfile, level, name, namespace, pretty_print=True):
        if self.category == MixedContainer.CategoryText:
            # Prevent exporting empty content as empty lines.
            if self.value.strip(): 
                outfile.write(self.value)
        elif self.category == MixedContainer.CategorySimple:
            self.exportSimple(outfile, level, name)
        else:    # category == MixedContainer.CategoryComplex
            self.value.export(outfile, level, namespace, name, pretty_print)
    def exportSimple(self, outfile, level, name):
        if self.content_type == MixedContainer.TypeString:
            outfile.write('<%s>%s</%s>' % (self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeInteger or \
                self.content_type == MixedContainer.TypeBoolean:
            outfile.write('<%s>%d</%s>' % (self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeFloat or \
                self.content_type == MixedContainer.TypeDecimal:
            outfile.write('<%s>%f</%s>' % (self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeDouble:
            outfile.write('<%s>%g</%s>' % (self.name, self.value, self.name))
    def exportLiteral(self, outfile, level, name):
        if self.category == MixedContainer.CategoryText:
            showIndent(outfile, level)
            outfile.write('model_.MixedContainer(%d, %d, "%s", "%s"),\n' % \
                (self.category, self.content_type, self.name, self.value))
        elif self.category == MixedContainer.CategorySimple:
            showIndent(outfile, level)
            outfile.write('model_.MixedContainer(%d, %d, "%s", "%s"),\n' % \
                (self.category, self.content_type, self.name, self.value))
        else:    # category == MixedContainer.CategoryComplex
            showIndent(outfile, level)
            outfile.write('model_.MixedContainer(%d, %d, "%s",\n' % \
                (self.category, self.content_type, self.name,))
            self.value.exportLiteral(outfile, level + 1)
            showIndent(outfile, level)
            outfile.write(')\n')


class MemberSpec_(object):
    def __init__(self, name='', data_type='', container=0):
        self.name = name
        self.data_type = data_type
        self.container = container
    def set_name(self, name): self.name = name
    def get_name(self): return self.name
    def set_data_type(self, data_type): self.data_type = data_type
    def get_data_type_chain(self): return self.data_type
    def get_data_type(self):
        if isinstance(self.data_type, list):
            if len(self.data_type) > 0:
                return self.data_type[-1]
            else:
                return 'xs:string'
        else:
            return self.data_type
    def set_container(self, container): self.container = container
    def get_container(self): return self.container

def cast_(typ, value):
    if typ is None or value is None:
        return value
    return typ(value)

#
# Data representation classes.
#

class IdentifierType(GeneratedsSuper):
    member_data_items_ = [
        MemberSpec_('schemeDataURI', 'xsd:anyURI', 0),
        MemberSpec_('schemeID', 'xsd:normalizedString', 0),
        MemberSpec_('schemeAgencyName', 'xsd:string', 0),
        MemberSpec_('schemeAgencyID', 'xsd:normalizedString', 0),
        MemberSpec_('schemeName', 'xsd:string', 0),
        MemberSpec_('schemeVersionID', 'xsd:normalizedString', 0),
        MemberSpec_('schemeURI', 'xsd:anyURI', 0),
        MemberSpec_('valueOf_', 'xsd:normalizedString', 0),
        ]
    subclass = None
    superclass = None
    def __init__(self, schemeDataURI=None, schemeID=None, schemeAgencyName=None, schemeAgencyID=None, schemeName=None, schemeVersionID=None, schemeURI=None, valueOf_=None, extensiontype_=None):
        self.schemeDataURI = cast_(None, schemeDataURI)
        self.schemeID = cast_(None, schemeID)
        self.schemeAgencyName = cast_(None, schemeAgencyName)
        self.schemeAgencyID = cast_(None, schemeAgencyID)
        self.schemeName = cast_(None, schemeName)
        self.schemeVersionID = cast_(None, schemeVersionID)
        self.schemeURI = cast_(None, schemeURI)
        self.valueOf_ = valueOf_
        self.extensiontype_ = extensiontype_
    def factory(*args_, **kwargs_):
        if IdentifierType.subclass:
            return IdentifierType.subclass(*args_, **kwargs_)
        else:
            return IdentifierType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_schemeDataURI(self): return self.schemeDataURI
    def set_schemeDataURI(self, schemeDataURI): self.schemeDataURI = schemeDataURI
    def get_schemeID(self): return self.schemeID
    def set_schemeID(self, schemeID): self.schemeID = schemeID
    def get_schemeAgencyName(self): return self.schemeAgencyName
    def set_schemeAgencyName(self, schemeAgencyName): self.schemeAgencyName = schemeAgencyName
    def get_schemeAgencyID(self): return self.schemeAgencyID
    def set_schemeAgencyID(self, schemeAgencyID): self.schemeAgencyID = schemeAgencyID
    def get_schemeName(self): return self.schemeName
    def set_schemeName(self, schemeName): self.schemeName = schemeName
    def get_schemeVersionID(self): return self.schemeVersionID
    def set_schemeVersionID(self, schemeVersionID): self.schemeVersionID = schemeVersionID
    def get_schemeURI(self): return self.schemeURI
    def set_schemeURI(self, schemeURI): self.schemeURI = schemeURI
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def get_extensiontype_(self): return self.extensiontype_
    def set_extensiontype_(self, extensiontype_): self.extensiontype_ = extensiontype_
    def export(self, outfile, level, namespace_='', name_='IdentifierType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='IdentifierType')
        if self.hasContent_():
            outfile.write('>')
            outfile.write(str(self.valueOf_).encode(ExternalEncoding))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='IdentifierType'):
        if self.schemeDataURI is not None and 'schemeDataURI' not in already_processed:
            already_processed.append('schemeDataURI')
            outfile.write(' schemeDataURI=%s' % (self.gds_format_string(quote_attrib(self.schemeDataURI).encode(ExternalEncoding), input_name='schemeDataURI'), ))
        if self.schemeID is not None and 'schemeID' not in already_processed:
            already_processed.append('schemeID')
            outfile.write(' schemeID=%s' % (self.gds_format_string(quote_attrib(self.schemeID).encode(ExternalEncoding), input_name='schemeID'), ))
        if self.schemeAgencyName is not None and 'schemeAgencyName' not in already_processed:
            already_processed.append('schemeAgencyName')
            outfile.write(' schemeAgencyName=%s' % (self.gds_format_string(quote_attrib(self.schemeAgencyName).encode(ExternalEncoding), input_name='schemeAgencyName'), ))
        if self.schemeAgencyID is not None and 'schemeAgencyID' not in already_processed:
            already_processed.append('schemeAgencyID')
            outfile.write(' schemeAgencyID=%s' % (self.gds_format_string(quote_attrib(self.schemeAgencyID).encode(ExternalEncoding), input_name='schemeAgencyID'), ))
        if self.schemeName is not None and 'schemeName' not in already_processed:
            already_processed.append('schemeName')
            outfile.write(' schemeName=%s' % (self.gds_format_string(quote_attrib(self.schemeName).encode(ExternalEncoding), input_name='schemeName'), ))
        if self.schemeVersionID is not None and 'schemeVersionID' not in already_processed:
            already_processed.append('schemeVersionID')
            outfile.write(' schemeVersionID=%s' % (self.gds_format_string(quote_attrib(self.schemeVersionID).encode(ExternalEncoding), input_name='schemeVersionID'), ))
        if self.schemeURI is not None and 'schemeURI' not in already_processed:
            already_processed.append('schemeURI')
            outfile.write(' schemeURI=%s' % (self.gds_format_string(quote_attrib(self.schemeURI).encode(ExternalEncoding), input_name='schemeURI'), ))
        if self.extensiontype_ is not None and 'xsi:type' not in already_processed:
            already_processed.append('xsi:type')
            outfile.write(' xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"')
            outfile.write(' xsi:type="%s"' % self.extensiontype_)
    def exportChildren(self, outfile, level, namespace_='', name_='IdentifierType', fromsubclass_=False, pretty_print=True):
        pass
    def hasContent_(self):
        if (
            self.valueOf_
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='IdentifierType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
        showIndent(outfile, level)
        outfile.write('valueOf_ = """%s""",\n' % (self.valueOf_,))
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.schemeDataURI is not None and 'schemeDataURI' not in already_processed:
            already_processed.append('schemeDataURI')
            showIndent(outfile, level)
            outfile.write('schemeDataURI = "%s",\n' % (self.schemeDataURI,))
        if self.schemeID is not None and 'schemeID' not in already_processed:
            already_processed.append('schemeID')
            showIndent(outfile, level)
            outfile.write('schemeID = "%s",\n' % (self.schemeID,))
        if self.schemeAgencyName is not None and 'schemeAgencyName' not in already_processed:
            already_processed.append('schemeAgencyName')
            showIndent(outfile, level)
            outfile.write('schemeAgencyName = "%s",\n' % (self.schemeAgencyName,))
        if self.schemeAgencyID is not None and 'schemeAgencyID' not in already_processed:
            already_processed.append('schemeAgencyID')
            showIndent(outfile, level)
            outfile.write('schemeAgencyID = "%s",\n' % (self.schemeAgencyID,))
        if self.schemeName is not None and 'schemeName' not in already_processed:
            already_processed.append('schemeName')
            showIndent(outfile, level)
            outfile.write('schemeName = "%s",\n' % (self.schemeName,))
        if self.schemeVersionID is not None and 'schemeVersionID' not in already_processed:
            already_processed.append('schemeVersionID')
            showIndent(outfile, level)
            outfile.write('schemeVersionID = "%s",\n' % (self.schemeVersionID,))
        if self.schemeURI is not None and 'schemeURI' not in already_processed:
            already_processed.append('schemeURI')
            showIndent(outfile, level)
            outfile.write('schemeURI = "%s",\n' % (self.schemeURI,))
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        self.valueOf_ = get_all_text_(node)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('schemeDataURI', node)
        if value is not None and 'schemeDataURI' not in already_processed:
            already_processed.append('schemeDataURI')
            self.schemeDataURI = value
        value = find_attr_value_('schemeID', node)
        if value is not None and 'schemeID' not in already_processed:
            already_processed.append('schemeID')
            self.schemeID = value
        value = find_attr_value_('schemeAgencyName', node)
        if value is not None and 'schemeAgencyName' not in already_processed:
            already_processed.append('schemeAgencyName')
            self.schemeAgencyName = value
        value = find_attr_value_('schemeAgencyID', node)
        if value is not None and 'schemeAgencyID' not in already_processed:
            already_processed.append('schemeAgencyID')
            self.schemeAgencyID = value
        value = find_attr_value_('schemeName', node)
        if value is not None and 'schemeName' not in already_processed:
            already_processed.append('schemeName')
            self.schemeName = value
        value = find_attr_value_('schemeVersionID', node)
        if value is not None and 'schemeVersionID' not in already_processed:
            already_processed.append('schemeVersionID')
            self.schemeVersionID = value
        value = find_attr_value_('schemeURI', node)
        if value is not None and 'schemeURI' not in already_processed:
            already_processed.append('schemeURI')
            self.schemeURI = value
        value = find_attr_value_('xsi:type', node)
        if value is not None and 'xsi:type' not in already_processed:
            already_processed.append('xsi:type')
            self.extensiontype_ = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class IdentifierType


class BillOfResourcesIDType(IdentifierType):
    member_data_items_ = [
        MemberSpec_('valueOf_', 'IdentifierType', 0),
        ]
    subclass = None
    superclass = IdentifierType
    def __init__(self, schemeDataURI=None, schemeID=None, schemeAgencyName=None, schemeAgencyID=None, schemeName=None, schemeVersionID=None, schemeURI=None, valueOf_=None):
        super(BillOfResourcesIDType, self).__init__(schemeDataURI, schemeID, schemeAgencyName, schemeAgencyID, schemeName, schemeVersionID, schemeURI, valueOf_, )
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if BillOfResourcesIDType.subclass:
            return BillOfResourcesIDType.subclass(*args_, **kwargs_)
        else:
            return BillOfResourcesIDType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def export(self, outfile, level, namespace_='', name_='BillOfResourcesIDType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='BillOfResourcesIDType')
        if self.hasContent_():
            outfile.write('>')
            outfile.write(str(self.valueOf_).encode(ExternalEncoding))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='BillOfResourcesIDType'):
        super(BillOfResourcesIDType, self).exportAttributes(outfile, level, already_processed, namespace_, name_='BillOfResourcesIDType')
    def exportChildren(self, outfile, level, namespace_='', name_='BillOfResourcesIDType', fromsubclass_=False, pretty_print=True):
        super(BillOfResourcesIDType, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        pass
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(BillOfResourcesIDType, self).hasContent_()
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='BillOfResourcesIDType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
        showIndent(outfile, level)
        outfile.write('valueOf_ = """%s""",\n' % (self.valueOf_,))
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        super(BillOfResourcesIDType, self).exportLiteralAttributes(outfile, level, already_processed, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        super(BillOfResourcesIDType, self).exportLiteralChildren(outfile, level, name_)
        pass
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        self.valueOf_ = get_all_text_(node)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        super(BillOfResourcesIDType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class BillOfResourcesIDType


class BillOfMaterialIDType(IdentifierType):
    member_data_items_ = [
        MemberSpec_('valueOf_', 'IdentifierType', 0),
        ]
    subclass = None
    superclass = IdentifierType
    def __init__(self, schemeDataURI=None, schemeID=None, schemeAgencyName=None, schemeAgencyID=None, schemeName=None, schemeVersionID=None, schemeURI=None, valueOf_=None):
        super(BillOfMaterialIDType, self).__init__(schemeDataURI, schemeID, schemeAgencyName, schemeAgencyID, schemeName, schemeVersionID, schemeURI, valueOf_, )
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if BillOfMaterialIDType.subclass:
            return BillOfMaterialIDType.subclass(*args_, **kwargs_)
        else:
            return BillOfMaterialIDType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def export(self, outfile, level, namespace_='', name_='BillOfMaterialIDType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='BillOfMaterialIDType')
        if self.hasContent_():
            outfile.write('>')
            outfile.write(str(self.valueOf_).encode(ExternalEncoding))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='', name_='BillOfMaterialIDType'):
        super(BillOfMaterialIDType, self).exportAttributes(outfile, level, already_processed, namespace_, name_='BillOfMaterialIDType')
    def exportChildren(self, outfile, level, namespace_='', name_='BillOfMaterialIDType', fromsubclass_=False, pretty_print=True):
        super(BillOfMaterialIDType, self).exportChildren(outfile, level, namespace_, name_, True, pretty_print=pretty_print)
        pass
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(BillOfMaterialIDType, self).hasContent_()
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='BillOfMaterialIDType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
        showIndent(outfile, level)
        outfile.write('valueOf_ = """%s""",\n' % (self.valueOf_,))
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        super(BillOfMaterialIDType, self).exportLiteralAttributes(outfile, level, already_processed, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        super(BillOfMaterialIDType, self).exportLiteralChildren(outfile, level, name_)
        pass
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        self.valueOf_ = get_all_text_(node)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        super(BillOfMaterialIDType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class BillOfMaterialIDType


USAGE_TEXT = """
Usage: python <Parser>.py [ -s ] <in_xml_file>
"""

def usage():
    print USAGE_TEXT
    sys.exit(1)


def get_root_tag(node):
    tag = Tag_pattern_.match(node.tag).groups()[-1]
    rootClass = globals().get(tag)
    return tag, rootClass


def parse(inFileName):
    doc = parsexml_(inFileName)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'IdentifierType'
        rootClass = IdentifierType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
##     sys.stdout.write('<?xml version="1.0" ?>\n')
##     rootObj.export(sys.stdout, 0, name_=rootTag,
##         namespacedef_='',
##         pretty_print=True)
    return rootObj


def parseString(inString):
    from StringIO import StringIO
    doc = parsexml_(StringIO(inString))
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'IdentifierType'
        rootClass = IdentifierType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
##     sys.stdout.write('<?xml version="1.0" ?>\n')
##     rootObj.export(sys.stdout, 0, name_="IdentifierType",
##         namespacedef_='')
    return rootObj


def parseLiteral(inFileName):
    doc = parsexml_(inFileName)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'IdentifierType'
        rootClass = IdentifierType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
##     sys.stdout.write('#from simplecontent_restriction2_sup import *\n\n')
##     sys.stdout.write('import simplecontent_restriction2_sup as model_\n\n')
##     sys.stdout.write('rootObj = model_.rootTag(\n')
##     rootObj.exportLiteral(sys.stdout, 0, name_=rootTag)
##     sys.stdout.write(')\n')
    return rootObj


def main():
    args = sys.argv[1:]
    if len(args) == 1:
        parse(args[0])
    else:
        usage()


if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    main()


__all__ = [
    "BillOfMaterialIDType",
    "BillOfResourcesIDType",
    "IdentifierType"
    ]
