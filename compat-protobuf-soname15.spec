#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : compat-protobuf-soname15
Version  : 3.5.1
Release  : 1
URL      : https://github.com/google/protobuf/archive/v3.5.1.tar.gz
Source0  : https://github.com/google/protobuf/archive/v3.5.1.tar.gz
Summary  : Google's Data Interchange Format
Group    : Development/Tools
License  : BSD-3-Clause
Requires: compat-protobuf-soname15-bin
Requires: compat-protobuf-soname15-lib
Requires: compat-protobuf-soname15-license
Requires: setuptools
Requires: six
BuildRequires : automake
BuildRequires : automake-dev
BuildRequires : cmake
BuildRequires : emacs
BuildRequires : gettext-bin
BuildRequires : go
BuildRequires : libtool
BuildRequires : libtool-dev
BuildRequires : m4
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pkg-config-dev
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : six
BuildRequires : zlib-dev
Patch1: 0001-Add-gmock-gtest-at-1.7.0.patch
Patch2: 0002-Ensure-everything-can-build-in-tree.patch
Patch3: 0003-Add-gtest-symlink-to-account-for-the-rest-of-the-bro.patch

%description
This is the 'v2' C++ implementation for python proto2.
It is active when:
PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=cpp
PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION_VERSION=2

%package bin
Summary: bin components for the compat-protobuf-soname15 package.
Group: Binaries
Requires: compat-protobuf-soname15-license

%description bin
bin components for the compat-protobuf-soname15 package.


%package dev
Summary: dev components for the compat-protobuf-soname15 package.
Group: Development
Requires: compat-protobuf-soname15-lib
Requires: compat-protobuf-soname15-bin
Provides: compat-protobuf-soname15-devel

%description dev
dev components for the compat-protobuf-soname15 package.


%package lib
Summary: lib components for the compat-protobuf-soname15 package.
Group: Libraries
Requires: compat-protobuf-soname15-license

%description lib
lib components for the compat-protobuf-soname15 package.


%package license
Summary: license components for the compat-protobuf-soname15 package.
Group: Default

%description license
license components for the compat-protobuf-soname15 package.


%prep
%setup -q -n protobuf-3.5.1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1530938823
%autogen --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1530938823
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/compat-protobuf-soname15
cp LICENSE %{buildroot}/usr/share/doc/compat-protobuf-soname15/LICENSE
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
%exclude /usr/bin/protoc

%files dev
%defattr(-,root,root,-)
%exclude /usr/include/google/protobuf/any.h
%exclude /usr/include/google/protobuf/any.pb.h
%exclude /usr/include/google/protobuf/any.proto
%exclude /usr/include/google/protobuf/api.pb.h
%exclude /usr/include/google/protobuf/api.proto
%exclude /usr/include/google/protobuf/arena.h
%exclude /usr/include/google/protobuf/arena_impl.h
%exclude /usr/include/google/protobuf/arenastring.h
%exclude /usr/include/google/protobuf/compiler/code_generator.h
%exclude /usr/include/google/protobuf/compiler/command_line_interface.h
%exclude /usr/include/google/protobuf/compiler/cpp/cpp_generator.h
%exclude /usr/include/google/protobuf/compiler/csharp/csharp_generator.h
%exclude /usr/include/google/protobuf/compiler/csharp/csharp_names.h
%exclude /usr/include/google/protobuf/compiler/importer.h
%exclude /usr/include/google/protobuf/compiler/java/java_generator.h
%exclude /usr/include/google/protobuf/compiler/java/java_names.h
%exclude /usr/include/google/protobuf/compiler/javanano/javanano_generator.h
%exclude /usr/include/google/protobuf/compiler/js/js_generator.h
%exclude /usr/include/google/protobuf/compiler/js/well_known_types_embed.h
%exclude /usr/include/google/protobuf/compiler/objectivec/objectivec_generator.h
%exclude /usr/include/google/protobuf/compiler/objectivec/objectivec_helpers.h
%exclude /usr/include/google/protobuf/compiler/parser.h
%exclude /usr/include/google/protobuf/compiler/php/php_generator.h
%exclude /usr/include/google/protobuf/compiler/plugin.h
%exclude /usr/include/google/protobuf/compiler/plugin.pb.h
%exclude /usr/include/google/protobuf/compiler/plugin.proto
%exclude /usr/include/google/protobuf/compiler/python/python_generator.h
%exclude /usr/include/google/protobuf/compiler/ruby/ruby_generator.h
%exclude /usr/include/google/protobuf/descriptor.h
%exclude /usr/include/google/protobuf/descriptor.pb.h
%exclude /usr/include/google/protobuf/descriptor.proto
%exclude /usr/include/google/protobuf/descriptor_database.h
%exclude /usr/include/google/protobuf/duration.pb.h
%exclude /usr/include/google/protobuf/duration.proto
%exclude /usr/include/google/protobuf/dynamic_message.h
%exclude /usr/include/google/protobuf/empty.pb.h
%exclude /usr/include/google/protobuf/empty.proto
%exclude /usr/include/google/protobuf/extension_set.h
%exclude /usr/include/google/protobuf/field_mask.pb.h
%exclude /usr/include/google/protobuf/field_mask.proto
%exclude /usr/include/google/protobuf/generated_enum_reflection.h
%exclude /usr/include/google/protobuf/generated_enum_util.h
%exclude /usr/include/google/protobuf/generated_message_reflection.h
%exclude /usr/include/google/protobuf/generated_message_table_driven.h
%exclude /usr/include/google/protobuf/generated_message_util.h
%exclude /usr/include/google/protobuf/has_bits.h
%exclude /usr/include/google/protobuf/io/coded_stream.h
%exclude /usr/include/google/protobuf/io/gzip_stream.h
%exclude /usr/include/google/protobuf/io/printer.h
%exclude /usr/include/google/protobuf/io/strtod.h
%exclude /usr/include/google/protobuf/io/tokenizer.h
%exclude /usr/include/google/protobuf/io/zero_copy_stream.h
%exclude /usr/include/google/protobuf/io/zero_copy_stream_impl.h
%exclude /usr/include/google/protobuf/io/zero_copy_stream_impl_lite.h
%exclude /usr/include/google/protobuf/map.h
%exclude /usr/include/google/protobuf/map_entry.h
%exclude /usr/include/google/protobuf/map_entry_lite.h
%exclude /usr/include/google/protobuf/map_field.h
%exclude /usr/include/google/protobuf/map_field_inl.h
%exclude /usr/include/google/protobuf/map_field_lite.h
%exclude /usr/include/google/protobuf/map_type_handler.h
%exclude /usr/include/google/protobuf/message.h
%exclude /usr/include/google/protobuf/message_lite.h
%exclude /usr/include/google/protobuf/metadata.h
%exclude /usr/include/google/protobuf/metadata_lite.h
%exclude /usr/include/google/protobuf/reflection.h
%exclude /usr/include/google/protobuf/reflection_ops.h
%exclude /usr/include/google/protobuf/repeated_field.h
%exclude /usr/include/google/protobuf/service.h
%exclude /usr/include/google/protobuf/source_context.pb.h
%exclude /usr/include/google/protobuf/source_context.proto
%exclude /usr/include/google/protobuf/struct.pb.h
%exclude /usr/include/google/protobuf/struct.proto
%exclude /usr/include/google/protobuf/stubs/atomic_sequence_num.h
%exclude /usr/include/google/protobuf/stubs/atomicops.h
%exclude /usr/include/google/protobuf/stubs/atomicops_internals_arm64_gcc.h
%exclude /usr/include/google/protobuf/stubs/atomicops_internals_arm_gcc.h
%exclude /usr/include/google/protobuf/stubs/atomicops_internals_arm_qnx.h
%exclude /usr/include/google/protobuf/stubs/atomicops_internals_generic_c11_atomic.h
%exclude /usr/include/google/protobuf/stubs/atomicops_internals_generic_gcc.h
%exclude /usr/include/google/protobuf/stubs/atomicops_internals_mips_gcc.h
%exclude /usr/include/google/protobuf/stubs/atomicops_internals_power.h
%exclude /usr/include/google/protobuf/stubs/atomicops_internals_ppc_gcc.h
%exclude /usr/include/google/protobuf/stubs/atomicops_internals_solaris.h
%exclude /usr/include/google/protobuf/stubs/atomicops_internals_tsan.h
%exclude /usr/include/google/protobuf/stubs/atomicops_internals_x86_gcc.h
%exclude /usr/include/google/protobuf/stubs/atomicops_internals_x86_msvc.h
%exclude /usr/include/google/protobuf/stubs/bytestream.h
%exclude /usr/include/google/protobuf/stubs/callback.h
%exclude /usr/include/google/protobuf/stubs/casts.h
%exclude /usr/include/google/protobuf/stubs/common.h
%exclude /usr/include/google/protobuf/stubs/fastmem.h
%exclude /usr/include/google/protobuf/stubs/hash.h
%exclude /usr/include/google/protobuf/stubs/logging.h
%exclude /usr/include/google/protobuf/stubs/macros.h
%exclude /usr/include/google/protobuf/stubs/mutex.h
%exclude /usr/include/google/protobuf/stubs/once.h
%exclude /usr/include/google/protobuf/stubs/platform_macros.h
%exclude /usr/include/google/protobuf/stubs/port.h
%exclude /usr/include/google/protobuf/stubs/scoped_ptr.h
%exclude /usr/include/google/protobuf/stubs/shared_ptr.h
%exclude /usr/include/google/protobuf/stubs/singleton.h
%exclude /usr/include/google/protobuf/stubs/status.h
%exclude /usr/include/google/protobuf/stubs/stl_util.h
%exclude /usr/include/google/protobuf/stubs/stringpiece.h
%exclude /usr/include/google/protobuf/stubs/template_util.h
%exclude /usr/include/google/protobuf/stubs/type_traits.h
%exclude /usr/include/google/protobuf/text_format.h
%exclude /usr/include/google/protobuf/timestamp.pb.h
%exclude /usr/include/google/protobuf/timestamp.proto
%exclude /usr/include/google/protobuf/type.pb.h
%exclude /usr/include/google/protobuf/type.proto
%exclude /usr/include/google/protobuf/unknown_field_set.h
%exclude /usr/include/google/protobuf/util/delimited_message_util.h
%exclude /usr/include/google/protobuf/util/field_comparator.h
%exclude /usr/include/google/protobuf/util/field_mask_util.h
%exclude /usr/include/google/protobuf/util/json_util.h
%exclude /usr/include/google/protobuf/util/message_differencer.h
%exclude /usr/include/google/protobuf/util/time_util.h
%exclude /usr/include/google/protobuf/util/type_resolver.h
%exclude /usr/include/google/protobuf/util/type_resolver_util.h
%exclude /usr/include/google/protobuf/wire_format.h
%exclude /usr/include/google/protobuf/wire_format_lite.h
%exclude /usr/include/google/protobuf/wire_format_lite_inl.h
%exclude /usr/include/google/protobuf/wrappers.pb.h
%exclude /usr/include/google/protobuf/wrappers.proto
%exclude /usr/lib64/libprotobuf-lite.so
%exclude /usr/lib64/libprotobuf.so
%exclude /usr/lib64/libprotoc.so
%exclude /usr/lib64/pkgconfig/protobuf-lite.pc
%exclude /usr/lib64/pkgconfig/protobuf.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libprotobuf-lite.so.15
/usr/lib64/libprotobuf-lite.so.15.0.1
/usr/lib64/libprotobuf.so.15
/usr/lib64/libprotobuf.so.15.0.1
/usr/lib64/libprotoc.so.15
/usr/lib64/libprotoc.so.15.0.1

%files license
%defattr(-,root,root,-)
%exclude /usr/share/doc/compat-protobuf-soname15/LICENSE