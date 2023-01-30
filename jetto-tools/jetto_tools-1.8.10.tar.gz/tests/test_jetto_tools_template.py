import pytest
import unittest.mock as mock
import os.path
import pathlib
import subprocess
import shutil
import jetto_tools.template as template
from jetto_tools.jset import JSET, ExtraNamelistItem
from jetto_tools.namelist import Namelist
from jetto_tools.lookup import ValidationError


class TestTemplateFileInterfaces:
    """Test that the template's file access interfaces behave as expected"""
    @pytest.fixture()
    def jset(self, mocker):
        return mocker.MagicMock(spec=JSET, restart=False)

    @pytest.fixture()
    def jetto_namelist(self, mocker):
        return mocker.MagicMock(spec=Namelist, return_value=True)

    @pytest.fixture()
    def sanco_namelist(self, mocker):
        return mocker.MagicMock(spec=Namelist, return_value=True)

    @pytest.fixture()
    def lookup(self):
        return {}

    @pytest.fixture()
    def template_under_test(self, jset, jetto_namelist, lookup, sanco_namelist):
        return template.Template(jset, jetto_namelist, lookup, sanco_namelist=sanco_namelist)

    template_attrs = ['jset', 'namelist', 'lookup', 'sanco_namelist']

    @pytest.mark.parametrize('attr', template_attrs)
    def test_can_retrieve_attribute_from_template(self, attr, template_under_test):
        _ = getattr(template_under_test, attr)

    @pytest.mark.parametrize('attr', template_attrs)
    def test_raises_if_attempt_to_modify_attr(self, attr, template_under_test):
        with pytest.raises(AttributeError):
            setattr(template_under_test, attr, None)

    def test_retrieved_jset_is_the_same_as_supplied(self, template_under_test, jset):
        assert jset is template_under_test.jset

    def test_retrieved_namelist_is_same_as_supplied(self, template_under_test, jetto_namelist):
        assert jetto_namelist is template_under_test.namelist

    def test_retrieved_lookup_is_same_as_supplied(self, template_under_test, lookup):
        assert lookup is template_under_test.lookup

    def test_retrieved_sanco_namelist_is_same_as_supplied(self, template_under_test, sanco_namelist):
        assert sanco_namelist is template_under_test.sanco_namelist

    def test_retrieved_sanco_namelist_is_none_if_omitted(self, jset, jetto_namelist, lookup):
        jset.sanco = False

        t = template.Template(jset, jetto_namelist, lookup)

        assert t.sanco_namelist is None

    def test_can_retrieve_false_catalogued_flag(self, template_under_test):
        assert template_under_test.catalogue_id is None

    def test_can_retrieve_valid_catalogued_flag(self, jset, jetto_namelist, lookup, sanco_namelist):
        t = template.Template(jset, jetto_namelist, lookup, sanco_namelist, catalogue_id='foo')

        assert t.catalogue_id == 'foo'


class TestJettoRegularParamValidation:
    """Test that Jetto namelist parameters (i.e. those not found in the JSET Jetto extra namelists) are validated as
    expected"""

    @pytest.fixture()
    def jset(self, mocker):
        m = mocker.MagicMock(spec=JSET)
        m.__getitem__.return_value = 0
        m.__contains__.return_value = True
        m.sanco_extras = {}
        m.extras = {}
        m.impurities = False

        return m

    @pytest.fixture()
    def jetto_namelist(self, mocker):
        m = mocker.MagicMock(spec=Namelist, return_value=True)
        m.exists.return_value = True
        m.namelist_lookup.return_value = 'NLIST'

        return m

    @pytest.fixture()
    def sanco_namelist(self, mocker):
        m = mocker.MagicMock(spec=Namelist, return_value=True)
        m.exists.return_value = False
        m.namelist_lookup.return_value = None

        return m

    @pytest.fixture()
    def lookup(self):
        return {
            'param': {
                'jset_id': 'Panel.Param',
                'nml_id': {
                    'namelist': 'NLIST',
                    'field': 'FIELD'
                },
                'type': 'int',
                'dimension': 'scalar'
            }
        }

    def test_passes(self, jset, jetto_namelist, lookup):
        _ = template.Template(jset, jetto_namelist, lookup)

    def test_fails_if_parameter_not_in_jset(self, jset, jetto_namelist, lookup):
        jset.__contains__.return_value = False

        with pytest.raises(template.TemplateError):
            _ = template.Template(jset, jetto_namelist, lookup)

    def test_fails_if_parameter_not_in_jetto_namelist(self, jset, jetto_namelist, lookup):
        jetto_namelist.exists.return_value = False
        jetto_namelist.namelist_lookup.return_value = None

        with pytest.raises(template.TemplateError):
            _ = template.Template(jset, jetto_namelist, lookup)

    def test_fails_if_parameter_is_vector(self, jset, jetto_namelist, lookup):
        lookup['param']['dimension'] = 'vector'

        with pytest.raises(template.TemplateError):
            _ = template.Template(jset, jetto_namelist, lookup)

    def test_passes_if_integer_param_can_be_converted(self, jset, jetto_namelist, lookup):
        jset.__getitem__.return_value = 1
        lookup['param']['type'] = 'real'

        _ = template.Template(jset, jetto_namelist, lookup)

    def test_passes_if_float_param_can_be_converted(self, jset, jetto_namelist, lookup):
        jset.__getitem__.return_value = 1.0
        lookup['param']['type'] = 'int'

        _ = template.Template(jset, jetto_namelist, lookup)


class TestJettoExtraNamelistParamValidation:
    """Test that JETTO extra namelist parameters (i.e. those found in the JSET JETTO extra namelists) are validated as
     expected"""

    @pytest.fixture()
    def jset(self, mocker):
        m = mocker.MagicMock(spec=JSET)
        m.__contains__.return_value = False
        m.extras = {'FIELD': ExtraNamelistItem(0)}
        m.sanco_extras = {}
        m.sanco = False
        m.impurities = False

        return m

    @pytest.fixture()
    def jetto_namelist(self, mocker):
        m = mocker.MagicMock(spec=Namelist, return_value=True)
        m.exists.return_value = True
        m.namelist_lookup.return_value = 'NLIST'

        return m

    @pytest.fixture()
    def lookup(self):
        return {
            'param': {
                'jset_id': None,
                'nml_id': {
                    'namelist': 'NLIST',
                    'field': 'FIELD'
                },
                'type': 'int',
                'dimension': 'scalar'
            }
        }

    def test_passes(self, jset, jetto_namelist, lookup):
        _ = template.Template(jset, jetto_namelist, lookup)

    def test_fails_if_param_not_in_jetto_namelist(self, jset, jetto_namelist, lookup):
        jetto_namelist.exists.return_value = False
        jetto_namelist.namelist_lookup.return_value = None

        with pytest.raises(template.TemplateError):
            _ = template.Template(jset, jetto_namelist, lookup)

    def test_fails_if_param_not_in_jetto_extras(self, jset, jetto_namelist, lookup):
        jset.extras = {}

        with pytest.raises(template.TemplateError):
            _ = template.Template(jset, jetto_namelist, lookup)

    def test_passes_if_parameter_is_not_scalar(self, jset, jetto_namelist, lookup):
        lookup['param']['dimension'] = 'vector'
        jset.extras = {'FIELD': ExtraNamelistItem([1, 2, 3], 1)}

        _ = template.Template(jset, jetto_namelist, lookup)


class TestSancoRegularParamValidation:
    """Test that Sanco namelist parameters (i.e. those not found in the JSET Sacno extra namelists) are validated as
    expected"""

    @pytest.fixture()
    def jset(self, mocker):
        m = mocker.MagicMock(spec=JSET)
        m.__contains__.return_value = True
        m.__getitem__.return_value = 0
        m.sanco_extras = {}
        m.extras = {}

        return m

    @pytest.fixture()
    def jetto_namelist(self, mocker):
        m = mocker.MagicMock(spec=Namelist, return_value=True)
        m.exists.return_value = False
        m.namelist_lookup.return_value = None

        return m

    @pytest.fixture()
    def sanco_namelist(self, mocker):
        m = mocker.MagicMock(spec=Namelist, return_value=True)
        m.exists.return_value = True
        m.namelist_lookup.return_value = 'NLIST'

        return m

    @pytest.fixture()
    def lookup(self):
        return {
            'param': {
                'jset_id': 'Panel.Param',
                'nml_id': {
                    'namelist': 'NLIST',
                    'field': 'FIELD'
                },
                'type': 'int',
                'dimension': 'scalar'
            }
        }

    def test_passes(self, jset, jetto_namelist, lookup, sanco_namelist):
        _ = template.Template(jset, jetto_namelist, lookup, sanco_namelist=sanco_namelist)

    def test_fails_if_parameter_not_in_sanco_namelist(self, jset, jetto_namelist, lookup, sanco_namelist):
        sanco_namelist.exists.return_value = False
        sanco_namelist.namelist_lookup.return_value = None

        with pytest.raises(template.TemplateError):
            _ = template.Template(jset, jetto_namelist, lookup, sanco_namelist=sanco_namelist)

    def test_fails_if_parameter_not_in_sanco_extras(self, jset, jetto_namelist, lookup, sanco_namelist):
        jset.__contains__.return_value = False

        with pytest.raises(template.TemplateError):
            _ = template.Template(jset, jetto_namelist, lookup, sanco_namelist=sanco_namelist)

    def test_fails_if_parameter_is_vector(self, jset, jetto_namelist, lookup, sanco_namelist):
        lookup['param']['dimension'] = 'vector'

        with pytest.raises(template.TemplateError):
            _ = template.Template(jset, jetto_namelist, lookup, sanco_namelist=sanco_namelist)


class TestSancoExtraNamelistParamValidation:
    """Test that Sanco extra namelist parameters (i.e. those found in the JSET Sanco extra namelists) are validated as
     expected"""

    @pytest.fixture()
    def jset(self, mocker):
        m = mocker.MagicMock(spec=JSET)
        m.__contains__.return_value = True
        m.sanco_extras = {'FIELD': ExtraNamelistItem(0)}
        m.extras = {}

        return m

    @pytest.fixture()
    def jetto_namelist(self, mocker):
        m = mocker.MagicMock(spec=Namelist, return_value=True)
        m.exists.return_value = False
        m.namelist_lookup.return_value = None

        return m

    @pytest.fixture()
    def sanco_namelist(self, mocker):
        m = mocker.MagicMock(spec=Namelist, return_value=True)
        m.exists.return_value = True
        m.namelist_lookup.return_value = 'NLIST'

        return m

    @pytest.fixture()
    def lookup(self):
        return {
            'param': {
                'jset_id': None,
                'nml_id': {
                    'namelist': 'NLIST',
                    'field': 'FIELD'
                },
                'type': 'int',
                'dimension': 'scalar'
            }
        }

    def test_passes(self, jset, jetto_namelist, lookup, sanco_namelist):
        _ = template.Template(jset, jetto_namelist, lookup, sanco_namelist=sanco_namelist)

    def test_fails_if_sanco_omitted(self, jset, jetto_namelist, lookup):
        with pytest.raises(template.TemplateError):
            t = template.Template(jset, jetto_namelist, lookup)

    def test_fails_if_param_not_in_sanco_extras(self, jset, jetto_namelist,
                                                lookup, sanco_namelist):
        jset.sanco_extras = {}

        with pytest.raises(template.TemplateError):
            _ = template.Template(jset, jetto_namelist, lookup, sanco_namelist=sanco_namelist)

    def test_passes_if_parameter_is_not_scalar(self, jset, jetto_namelist, lookup, sanco_namelist):
        jset.sanco_extras = {'FIELD': ExtraNamelistItem([1, 2, 3], 1)}

        _ = template.Template(jset, jetto_namelist, lookup, sanco_namelist=sanco_namelist)


class TestLookupValidation:
    """Test that the Template classes validates the lookup prior to using it"""
    @pytest.fixture()
    def jset(self, mocker):
        m = mocker.MagicMock(spec=JSET)
        m.impurities = False
        m.sanco = False

        return m

    @pytest.fixture()
    def jetto_namelist(self, mocker):
        return mocker.MagicMock(spec=Namelist, return_value=True)

    @pytest.fixture()
    def lookup(self):
        return {}

    @mock.patch('jetto_tools.template.jetto_tools.lookup.validate')
    def test_template_validates_lookup(self, mock_validate, jset, jetto_namelist, lookup):
        t = template.Template(jset, jetto_namelist, lookup)

        mock_validate.assert_called_once_with(lookup)

    @mock.patch('jetto_tools.template.jetto_tools.lookup.validate')
    def test_template_raises_if_validation_fails(self, mock_validate, jset, jetto_namelist, lookup):
        mock_validate.side_effect = ValidationError

        with pytest.raises(template.TemplateError):
            _ = template.Template(jset, jetto_namelist, lookup)


class TestSancoAsImpuritiesSource:
    """Test that if sanco is configured as the impurities source, the SANCO namelist is required to exist"""

    @pytest.fixture()
    def jset(self, mocker):
        return mocker.MagicMock(spec=JSET)

    @pytest.fixture()
    def jetto_namelist(self, mocker):
        return mocker.MagicMock(spec=Namelist, return_value=True)

    @pytest.fixture()
    def sanco_namelist(self, mocker):
        return mocker.MagicMock(spec=Namelist, return_value=True)

    @pytest.fixture()
    def lookup(self):
        return {}

    def test_raises_if_sanco_namelist_missing(self, jset, jetto_namelist, lookup):
        jset.sanco = True
        jset.impurities = True

        with pytest.raises(template.TemplateError):
            _ = template.Template(jset, jetto_namelist, lookup)

    def test_passes_if_sanco_namelist_provided(self, jset, jetto_namelist, lookup, sanco_namelist):
        jset.sanco = True
        jset.impurities = True

        _ = template.Template(jset, jetto_namelist, lookup, sanco_namelist=sanco_namelist)


class TestExtraFileInterfaces:
    """Test that we can retrieve non-essential file paths from the template if they exist"""

    @pytest.fixture()
    def jset(self, mocker):
        m = mocker.MagicMock(spec=JSET)
        m.impurities = False
        m.sanco = False

        return m

    @pytest.fixture()
    def jetto_namelist(self, mocker):
        return mocker.MagicMock(spec=Namelist, return_value=True)

    @pytest.fixture()
    def lookup(self):
        return {}

    def test_no_extra_files(self, jset, jetto_namelist, lookup):
        t = template.Template(jset, jetto_namelist, lookup, extra_files=[])

        assert t.extra_files == {}

    def test_single_extra_file(self, jset, jetto_namelist, lookup):
        t = template.Template(jset, jetto_namelist, lookup, extra_files=['/path/to/jetto.ex'])

        assert t.extra_files == {'jetto.ex': '/path/to/jetto.ex'}

    def test_multiple_extra_files(self, jset, jetto_namelist, lookup):
        t = template.Template(jset, jetto_namelist, lookup, extra_files=['/path/to/jetto.ex', '/path/to/jetto.bnd'])

        assert t.extra_files == {'jetto.ex': '/path/to/jetto.ex', 'jetto.bnd': '/path/to/jetto.bnd'}

    def test_raises_if_extra_file_is_invalid(self, jset, jetto_namelist, lookup):
        with pytest.raises(template.TemplateError):
            _ = template.Template(jset, jetto_namelist, lookup, extra_files=['/path/to/jetto.bond'])


class TestLoadFromFiles:
    """Test that we can load a template from file paths"""
    @pytest.fixture()
    def jset_file(self, tmpdir):
        file = tmpdir.join('jetto.jset')
        file.write('JSET')

        return file

    @pytest.fixture()
    def jetto_namelist_file(self, tmpdir):
        file = tmpdir.join('jetto.in')
        file.write('JETTO NAMELIST')

        return file

    @pytest.fixture()
    def sanco_namelist_file(self, tmpdir):
        file = tmpdir.join('jetto.sin')
        file.write('SANCO NAMELIST')

        return file

    @pytest.fixture()
    def lookup_file(self, tmpdir):
        file = tmpdir.join('lookup.json')
        file.write('LOOKUP')

        return file

    @pytest.fixture()
    def extra_files(self, tmpdir):
        file_a = tmpdir.join('jetto.eqdsk')
        file_a.write('')

        file_b = tmpdir.join('jetto.sgrid')
        file_b.write('')

        return [file_a, file_b]

    @pytest.fixture()
    def jset(self, mocker):
        m = mocker.MagicMock(spec=JSET, restart=False)
        m.impurities = False

        return m

    @pytest.fixture()
    def jetto_namelist(self, mocker):
        return mocker.MagicMock(spec=Namelist, return_value=True)

    @pytest.fixture()
    def sanco_namelist(self, mocker):
        return mocker.MagicMock(spec=Namelist, return_value=True)

    @pytest.fixture()
    def lookup(self):
        return {}

    @pytest.fixture()
    def mocked_out_jset(self, jset):
        with mock.patch('jetto_tools.template.JSET') as _fixture:
            _fixture.return_value = jset

            yield _fixture

    @pytest.fixture()
    def mocked_out_namelist(self, jetto_namelist, sanco_namelist):
        with mock.patch('jetto_tools.template.Namelist') as _fixture:
            def return_namelist(contents):
                if contents == 'JETTO NAMELIST':
                    return jetto_namelist
                else:
                    return sanco_namelist
            _fixture.side_effect = return_namelist

            yield _fixture

    @pytest.fixture()
    def mocked_out_lookup(self, lookup):
        with mock.patch('jetto_tools.template.jetto_tools.lookup.from_file') as _fixture:
            _fixture.return_value = lookup

            yield _fixture

    @pytest.fixture()
    def all_mocks(self, mocked_out_jset, mocked_out_namelist, mocked_out_lookup):
        return mocked_out_jset, mocked_out_namelist, mocked_out_lookup

    @pytest.fixture()
    def mocked_out_template(self, mocked_out_jset):
        with mock.patch('jetto_tools.template.Template') as _fixture:
            _fixture.jset = mocked_out_jset

            yield _fixture

    def test_from_files_calls_jset_with_jset_file_contents(self, jset_file, jetto_namelist_file, lookup_file,
                                                           all_mocks, mocked_out_jset):
        _ = template.from_files(jset_file.strpath, jetto_namelist_file.strpath, lookup_file.strpath)

        mocked_out_jset.assert_called_once_with('JSET')

    def test_from_files_calls_namelist_with_namelist_file_contents(self, jset_file, jetto_namelist_file, lookup_file,
                                                                   all_mocks, mocked_out_namelist):
        _ = template.from_files(jset_file.strpath, jetto_namelist_file.strpath, lookup_file.strpath)

        mocked_out_namelist.assert_called_once_with('JETTO NAMELIST')

    def test_from_files_calls_lookup_with_lookup_file_contents(self, jset_file, jetto_namelist_file, lookup_file,
                                                               all_mocks, mocked_out_lookup):
        _ = template.from_files(jset_file.strpath, jetto_namelist_file.strpath, lookup_file.strpath)

        mocked_out_lookup.assert_called_once_with(pathlib.Path(lookup_file.strpath))

    def test_from_files_calls_namelist_with_sanco_file_contents(self, jset_file, jetto_namelist_file, lookup_file,
                                                                sanco_namelist_file, all_mocks, mocked_out_namelist):
        _ = template.from_files(jset_file.strpath, jetto_namelist_file.strpath, lookup_file.strpath,
                                sanco_namelist_path=sanco_namelist_file.strpath)

        mocked_out_namelist.has_calls([mock.call('JETTO NAMELIST'), mock.call('SANCO NAMELIST')])

    def test_passes_core_files_to_template(self, jset_file, jetto_namelist_file, lookup_file,
                                           jset, jetto_namelist, lookup, all_mocks):
        t = template.from_files(jset_file.strpath, jetto_namelist_file.strpath, lookup_file.strpath)

        assert (t.jset is jset) and (t.namelist is jetto_namelist) and (t.lookup is lookup) and \
               (t.sanco_namelist is None)

    def test_passes_sanco_namelist_to_template(self, jset_file, jetto_namelist_file, lookup_file,
                                               sanco_namelist_file, jset, jetto_namelist, lookup,
                                               sanco_namelist, all_mocks):
        t = template.from_files(jset_file.strpath, jetto_namelist_file.strpath, lookup_file.strpath,
                                sanco_namelist_file.strpath)

        assert (t.jset is jset) and (t.namelist is jetto_namelist) and (t.lookup is lookup) and \
               (t.sanco_namelist is sanco_namelist)

    def test_passes_extra_files_to_template(self, jset_file, jetto_namelist_file, lookup_file,
                                            sanco_namelist_file, jset, jetto_namelist, lookup,
                                            sanco_namelist, all_mocks, extra_files):
        file_a, file_b = extra_files
        files = [file.strpath for file in extra_files]

        t = template.from_files(jset_file.strpath, jetto_namelist_file.strpath, lookup_file.strpath,
                                sanco_namelist_file.strpath, extra_files=files)

        assert t.extra_files['jetto.eqdsk'] == file_a.strpath and t.extra_files['jetto.sgrid'] == file_b.strpath

    def test_raises_if_jset_file_does_not_exist(self, jset_file, jetto_namelist_file, lookup_file,
                                                sanco_namelist_file, jset, jetto_namelist, lookup,
                                                sanco_namelist, all_mocks):
        jset_file.remove()

        with pytest.raises(template.TemplateError):
            _ = template.from_files(jset_file.strpath, jetto_namelist_file.strpath, lookup_file.strpath,
                                    sanco_namelist_file.strpath)

    def test_raises_if_jetto_namelist_file_does_not_exist(self, jset_file, jetto_namelist_file, lookup_file,
                                                          sanco_namelist_file, jset, jetto_namelist, lookup,
                                                          sanco_namelist, all_mocks):
        jetto_namelist_file.remove()

        with pytest.raises(template.TemplateError):
            _ = template.from_files(jset_file.strpath, jetto_namelist_file.strpath, lookup_file.strpath,
                                    sanco_namelist_file.strpath)

    def test_raises_if_lookup_file_does_not_exist(self, jset_file, jetto_namelist_file, lookup_file,
                                                  sanco_namelist_file, jset, jetto_namelist, lookup,
                                                  sanco_namelist, all_mocks):
        lookup_file.remove()

        with pytest.raises(template.TemplateError):
            _ = template.from_files(jset_file.strpath, jetto_namelist_file.strpath, lookup_file.strpath,
                                    sanco_namelist_file.strpath)

    def test_raises_if_sanco_namelist_file_does_not_exist(self, jset_file, jetto_namelist_file, lookup_file,
                                                          sanco_namelist_file, jset, jetto_namelist, lookup,
                                                          sanco_namelist, all_mocks):
        sanco_namelist_file.remove()

        with pytest.raises(template.TemplateError):
            _ = template.from_files(jset_file.strpath, jetto_namelist_file.strpath, lookup_file.strpath,
                                    sanco_namelist_file.strpath)

    def test_raises_if_extra_file_does_not_exist(self, jset_file, jetto_namelist_file, lookup_file,
                                                 sanco_namelist_file, jset, jetto_namelist, lookup,
                                                 sanco_namelist, all_mocks, extra_files):
        files = [file.strpath for file in extra_files]
        _ = [file.remove() for file in extra_files]

        with pytest.raises(template.TemplateError):
            _ = template.from_files(jset_file.strpath, jetto_namelist_file.strpath, lookup_file.strpath,
                                    sanco_namelist_file.strpath, extra_files=extra_files)

    def test_calls_set_backwards_compatibility(self, jset_file, jetto_namelist_file, lookup_file,
                                               sanco_namelist_file, jset, jetto_namelist, lookup,
                                               sanco_namelist, all_mocks, extra_files, mocked_out_jset):
        _ = template.from_files(jset_file.strpath, jetto_namelist_file.strpath, lookup_file.strpath,
                                sanco_namelist_file.strpath, extra_files=extra_files)

        jset.set_backwards_compatibility.assert_called_once()

    def test_set_backwards_compatibility_not_called(self, jset_file, jetto_namelist_file, lookup_file,
                                                    sanco_namelist_file, jset, jetto_namelist, lookup,
                                                    sanco_namelist, all_mocks, extra_files, mocked_out_jset):
        jset.version_as_date = None

        _ = template.from_files(jset_file.strpath, jetto_namelist_file.strpath, lookup_file.strpath,
                                sanco_namelist_file.strpath, extra_files=extra_files)

        jset.set_backwards_compatibility.assert_not_called()

    @pytest.mark.parametrize('catalogue_id', [None, 'foo'])
    def test_passes_catalogue_id_to_template(self, jset_file, jetto_namelist_file, lookup_file,
                                             all_mocks, catalogue_id, mocked_out_template):
        t = template.from_files(jset_file.strpath, jetto_namelist_file.strpath, lookup_file.strpath,
                                catalogue_id=catalogue_id)

        assert mocked_out_template.call_args[1]['catalogue_id'] == catalogue_id


class TestLoadFromDirectory:
    """Test that we can load files from a directory containing a template"""
    @pytest.fixture()
    def template_dir(self, tmpdir):
        return tmpdir.mkdir('template')

    @pytest.fixture()
    def jset_file(self, template_dir):
        file = template_dir.join('jetto.jset')
        file.write('')

        return file

    @pytest.fixture()
    def jetto_namelist_file(self, template_dir):
        file = template_dir.join('jetto.in')
        file.write('')

        return file

    @pytest.fixture()
    def sanco_namelist_file(self, template_dir):
        file = template_dir.join('jetto.sin')
        file.write('')

        return file

    @pytest.fixture()
    def lookup_file(self, template_dir):
        file = template_dir.join('lookup.json')
        file.write('')

        return file

    def test_raises_if_directory_does_not_exist(self, template_dir):
        template_dir.remove()

        with pytest.raises(template.TemplateError):
            _ = template.from_directory(template_dir.strpath)

    def test_core_file_paths_are_passed_to_file_load(self, template_dir, jset_file, jetto_namelist_file, lookup_file):
        with mock.patch('jetto_tools.template.from_files', spec=template.from_files) as mock_load:
            _ = template.from_directory(template_dir.strpath)

            mock_load.assert_called_once_with(jset_file.strpath, jetto_namelist_file.strpath, lookup_file.strpath,
                                              None, [], None)

    def test_sanco_namelist_path_is_passed_to_file_load_if_it_exists(self, template_dir, jset_file, jetto_namelist_file,
                                                                     lookup_file, sanco_namelist_file):
        with mock.patch('jetto_tools.template.from_files', spec=template.from_files) as mock_load:
            _ = template.from_directory(template_dir.strpath)

            mock_load.assert_called_once_with(jset_file.strpath, jetto_namelist_file.strpath, lookup_file.strpath,
                                              sanco_namelist_file.strpath, [], None)

    @pytest.mark.parametrize('extra_file', ['jetto.bnd', 'jetto.ec', 'jetto.eqfile', 'jetto.eqrestart', 'jetto.ext',
                                            'jetto.lh', 'jetto.pset', 'jetto.str', 'jetto.sgrid', 'jetto.restart',
                                            'jetto.srestart', 'jetto.nbip', 'jetto.nbip1', 'jetto.nbip2', 'jetto.nbip3',
                                            'jetto.lhp', 'jetto.rfp', 'jetto.ecp', 'jetto.fbk', 'jetto.fbk2',
                                            'jetto.spec', 'jetto.beamionsource', 'jetto.mhddb', 'jetto.evp',
                                            'jetto.cup', 'jetto.vlp', 'jetto.tep', 'jetto.tip', 'jetto.eqt',
                                            'jetto.eqdsk', 'jetto.cbank', 'jetto.nbicfg', 'jetto.dse', 'jetto.ex'])
    def test_valid_jetto_extra_files_are_passed_to_file_load(self, extra_file, template_dir):
        file = template_dir.join(extra_file)
        file.write('')

        with mock.patch('jetto_tools.template.from_files', spec=template.from_files) as mock_load:
            _ = template.from_directory(template_dir.strpath)

            assert mock_load.call_args[1]['extra_files'] == [file.strpath]

    @pytest.mark.parametrize('extra_file', ['jetto_.eqdsk', 'jetto_foo.eqdsk', 'jetto_1.eqdsk'])
    def test_valid_jetto_eqdsk_extra_files_are_passed_to_file_load(self, extra_file, template_dir):
        file = template_dir.join(extra_file)
        file.write('')

        with mock.patch('jetto_tools.template.from_files', spec=template.from_files) as mock_load:
            _ = template.from_directory(template_dir.strpath)

            assert mock_load.call_args[1]['extra_files'] == [file.strpath]

    @pytest.mark.parametrize('extra_file', ['ascot.h5', 'ascot.accprv', 'ascot.cntl', 'ascot.endstate',
                                            'ascot.endstatefoo', 'ascot.endstate1'])
    def test_valid_ascot_extra_files_are_passed_to_file_load(self, extra_file, template_dir):
        file = template_dir.join(extra_file)
        file.write('')

        with mock.patch('jetto_tools.template.from_files', spec=template.from_files) as mock_load:
            _ = template.from_directory(template_dir.strpath)

            assert mock_load.call_args[1]['extra_files'] == [file.strpath]

    @pytest.mark.parametrize('extra_file', ['gray.data', 'graybeam.data'])
    def test_valid_gray_extra_files_are_passed_to_file_load(self, extra_file, template_dir):
        file = template_dir.join(extra_file)
        file.write('')

        with mock.patch('jetto_tools.template.from_files', spec=template.from_files) as mock_load:
            _ = template.from_directory(template_dir.strpath)

            assert mock_load.call_args[1]['extra_files'] == [file.strpath]

    @pytest.mark.parametrize('extra_file', ['eirene_nbi.elemente', 'eirene_nbi.neighbors', 'eirene_nbi.npco_char'])
    def test_valid_eirene_extra_files_are_passed_to_file_load(self, extra_file, template_dir):
        file = template_dir.join(extra_file)
        file.write('')

        with mock.patch('jetto_tools.template.from_files', spec=template.from_files) as mock_load:
            _ = template.from_directory(template_dir.strpath)

            assert mock_load.call_args[1]['extra_files'] == [file.strpath]

    @pytest.mark.parametrize('extra_file', ['createnl_nominal_ref.mat', 'createnl_dyn_out.mat',
                                            'createnl_coupling_init.diag'])
    def test_valid_create_extra_files_are_passed_to_file_load(self, extra_file, template_dir):
        file = template_dir.join(extra_file)
        file.write('')

        with mock.patch('jetto_tools.template.from_files', spec=template.from_files) as mock_load:
            _ = template.from_directory(template_dir.strpath)

            assert mock_load.call_args[1]['extra_files'] == [file.strpath]

    @pytest.mark.parametrize('extra_file', ['input.options', 'README', 'GridSHscalfac.txt', 'TCI_asym.dat',
                                            'imas_jetto_workflow.cfg', 'Ext_HCD_WF_config'])
    def test_valid_misc_extra_files_are_passed_to_file_load(self, extra_file, template_dir):
        file = template_dir.join(extra_file)
        file.write('')

        with mock.patch('jetto_tools.template.from_files', spec=template.from_files) as mock_load:
            _ = template.from_directory(template_dir.strpath)

            assert mock_load.call_args[1]['extra_files'] == [file.strpath]

    @pytest.mark.parametrize('catalogue_id', [None, 'foo'])
    def test_passes_catalogue_id_to_from_files(self, template_dir, jset_file, jetto_namelist_file, lookup_file,
                                               catalogue_id):
        with mock.patch('jetto_tools.template.from_files', spec=template.from_files) as mock_load:
            _ = template.from_directory(template_dir.strpath, catalogue_id=catalogue_id)

            assert mock_load.call_args[1]['catalogue_id'] == catalogue_id


class TestLoadFromCatalogue:
    """Test that we can load files from a catalogued location"""
    @pytest.fixture()
    def retrieve_script(self, fake_process):
        fake_process.register_subprocess(['retrieve', fake_process.any()],
                                         stdout=[],
                                         returncode=0)
        return fake_process

    @pytest.fixture()
    def mock_subprocess_run(self):
        with mock.patch('jetto_tools.template.subprocess.run') as mock_run:
            mock_run.return_value = mock.Mock(spec=subprocess.CompletedProcess)
            mock_run.return_value.returncode = 0

            yield mock_run

    @pytest.fixture()
    def owner(self):
        return 'sim'

    @pytest.fixture()
    def machine(self):
        return 'jet'

    @pytest.fixture()
    def shot(self):
        return 92398

    @pytest.fixture()
    def date(self):
        return 'dec1218'

    @pytest.fixture()
    def seq(self):
        return 2

    @pytest.fixture()
    def lookup(self, tmpdir):
        lkp = tmpdir.join('lookup.json')
        lkp.write('foo')

        return lkp

    @pytest.fixture()
    def args(self, owner, machine, shot, date, seq, lookup):
        return owner, machine, shot, date, seq, lookup.strpath

    @pytest.fixture()
    def mocked_out_from_directory(self):
        with mock.patch('jetto_tools.template.from_directory') as _fixture:
            _fixture.return_value = mock.MagicMock(spec=template.Template)

            yield _fixture

    @pytest.fixture()
    def retrieval_dir(self, tmpdir):
        return tmpdir.mkdir('jetto_retrieval')

    def test_call_made_to_retrieve_script(self, retrieve_script, args, mocked_out_from_directory):
        _ = template.from_catalogue(*args)

        assert len(retrieve_script.calls) == 1 and retrieve_script.calls[0][0] == 'retrieve'

    def test_raises_if_retrieve_script_fails(self, fake_process, args, mocked_out_from_directory):
        failing_retrieve_script = fake_process.register_subprocess(['retrieve', fake_process.any()],
                                                                   stdout=[],
                                                                   returncode=127)

        with pytest.raises(template.TemplateError):
            t = template.from_catalogue(*args)

    def test_machine_is_passed_to_retrieve_script(self, retrieve_script, args, mocked_out_from_directory, machine):
        _ = template.from_catalogue(*args)

        assert f'-m{machine}' in retrieve_script.calls[0]

    def test_owner_is_passed_to_retrieve_script(self, retrieve_script, args, mocked_out_from_directory, owner):
        _ = template.from_catalogue(*args)

        assert f'-o{owner}' in retrieve_script.calls[0]

    def test_code_is_passed_to_retrieve_script(self, retrieve_script, args, mocked_out_from_directory, owner):
        _ = template.from_catalogue(*args)

        assert '-Cjetto' in retrieve_script.calls[0]

    def test_required_args_are_passed_to_retrieve_script(self, retrieve_script, args, mocked_out_from_directory,
                                                         shot, date, seq):
        _ = template.from_catalogue(*args)

        assert all(arg in retrieve_script.calls[0] for arg in [f'{shot}', f'{date}', f'{seq}'])

    def test_continue_is_not_passed_to_retrieve_script(self, retrieve_script, args, mocked_out_from_directory):
        _ = template.from_catalogue(*args)

        assert '-c' not in retrieve_script.calls[0]

    def test_continue_is_passed_to_retrieve_script(self, retrieve_script, args, mocked_out_from_directory):
        _ = template.from_catalogue(*args, continue_run=True)

        assert '-c' in retrieve_script.calls[0]

    def test_calls_from_directory(self, retrieve_script, args, mocked_out_from_directory):
        _ = template.from_catalogue(*args)

        mocked_out_from_directory.assert_called_once()

    def test_creates_retrieval_dir_if_it_does_not_exist(self, args, mocked_out_from_directory,
                                                        mock_subprocess_run, retrieval_dir):
        retrieval_dir.remove()

        _ = template.from_catalogue(*args, continue_run=True, retrieval_dir=retrieval_dir)

        assert os.path.isdir(retrieval_dir.strpath)

    def test_empties_retrieval_dir_prior_to_use(self, args, mocked_out_from_directory,
                                                mock_subprocess_run, retrieval_dir):
        retrieval_dir.join('foo.txt').write('')

        _ = template.from_catalogue(*args, continue_run=True, retrieval_dir=retrieval_dir)

        assert not os.path.isfile(retrieval_dir.join('foo.txt').strpath)

    def test_retrieval_directory_used_in_retrieve_call(self, args, mocked_out_from_directory,
                                                       mock_subprocess_run, retrieval_dir):
        _ = template.from_catalogue(*args, continue_run=True, retrieval_dir=retrieval_dir)

        run_dir = mock_subprocess_run.call_args[1]['cwd']

        assert run_dir == retrieval_dir.strpath

    def test_retrieval_directory_passed_to_load_from_directory_call(self, args, mocked_out_from_directory,
                                                                    mock_subprocess_run, retrieval_dir):
        _ = template.from_catalogue(*args, continue_run=True, retrieval_dir=retrieval_dir)

        assert mocked_out_from_directory.call_args[0][0] == retrieval_dir.strpath

    def test_catalogue_id_passed_to_load_from_directory_call(self, args, mocked_out_from_directory,
                                                             mock_subprocess_run, retrieval_dir):
        _ = template.from_catalogue(*args, continue_run=True, retrieval_dir=retrieval_dir)

        assert mocked_out_from_directory.call_args[1]['catalogue_id'] == \
               f'{args[0]}/jetto/{args[1]}/{args[2]}/{args[3]}/seq-{args[4]}'

    def test_lookup_copied_into_retrieval_directory(self, args, mocked_out_from_directory, mock_subprocess_run, lookup):
        def check_lookup_file(dir, catalogue_id):
            with open(os.path.join(dir, 'lookup.json')) as f:
                assert f.read() == 'foo'

            return mock.MagicMock(spec=template.Template)

        mocked_out_from_directory.side_effect = check_lookup_file

        _ = template.from_catalogue(*args)

    def test_raises_if_lookup_does_not_exist(self, args, mocked_out_from_directory, mock_subprocess_run, lookup):
        lookup.remove()

        with pytest.raises(template.TemplateError):
            _ = template.from_catalogue(*args)

    def test_returns_result_of_from_directory_call(self, retrieve_script, args, mocked_out_from_directory):
        t = template.from_catalogue(*args)

        assert t is mocked_out_from_directory.return_value

    def test_calls_set_catalogued_files(self, retrieve_script, args, mocked_out_from_directory,
                                        owner, machine, shot, date, seq):
        mocked_out_from_directory.return_value = mock.MagicMock(spec=template.Template)
        mock_set_catalogued_files = mocked_out_from_directory.return_value.jset.set_catalogued_files

        _ = template.from_catalogue(*args)

        mock_set_catalogued_files.assert_called_once_with(owner, 'jetto', machine, shot, date, seq)

    @pytest.mark.parametrize('continue_', [True, False], ids=['Continue', 'Not continue'])
    def test_calls_set_restart_flags(self, retrieve_script, args, mocked_out_from_directory,
                                     owner, machine, shot, date, seq, continue_):
        mocked_out_from_directory.return_value = mock.MagicMock(spec=template.Template)
        mock_set_restart_flags = mocked_out_from_directory.return_value.jset.set_restart_flags

        _ = template.from_catalogue(*args, continue_run=continue_)

        mock_set_restart_flags.assert_called_once_with(continue_)
