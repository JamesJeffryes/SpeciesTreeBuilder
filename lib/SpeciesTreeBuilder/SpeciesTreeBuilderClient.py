# -*- coding: utf-8 -*-
############################################################
#
# Autogenerated by the KBase type compiler -
# any changes made here will be overwritten
#
############################################################

from __future__ import print_function
# the following is a hack to get the baseclient to import whether we're in a
# package or not. This makes pep8 unhappy hence the annotations.
try:
    # baseclient and this client are in a package
    from .baseclient import BaseClient as _BaseClient  # @UnusedImport
except:
    # no they aren't
    from baseclient import BaseClient as _BaseClient  # @Reimport


class SpeciesTreeBuilder(object):

    def __init__(
            self, url=None, timeout=30 * 60, user_id=None,
            password=None, token=None, ignore_authrc=False,
            trust_all_ssl_certificates=False,
            auth_svc='https://kbase.us/services/authorization/Sessions/Login'):
        if url is None:
            raise ValueError('A url is required')
        self._service_ver = None
        self._client = _BaseClient(
            url, timeout=timeout, user_id=user_id, password=password,
            token=token, ignore_authrc=ignore_authrc,
            trust_all_ssl_certificates=trust_all_ssl_certificates,
            auth_svc=auth_svc)

    def construct_species_tree(self, input, context=None):
        """
        Build a species tree out of a set of given genome references.
        :param input: instance of type "ConstructSpeciesTreeParams" (Input
           data type for construct_species_tree method. Method produces
           object of Tree type. new_genomes - (optional) the list of genome
           references to use in constructing a tree; either new_genomes or
           genomeset_ref field should be defined. genomeset_ref - (optional)
           reference to genomeset object; either new_genomes or genomeset_ref
           field should be defined. out_workspace - (required) the workspace
           to deposit the completed tree out_tree_id - (optional) the name of
           the newly constructed tree (will be random if not present or null)
           out_genomeset_ref - the name of the output genomeset object
           copy_genomes - 1 means copy genomes to user workspace; 0 means
           refer only to the public genomes use_ribosomal_s9_only -
           (optional) 1 means only one protein family (Ribosomal S9) is used
           for tree construction rather than all 49 improtant families,
           default value is 0. nearest_genome_count - (optional) defines
           maximum number of public genomes nearest to requested genomes that
           will show in output tree.) -> structure: parameter "new_genomes"
           of list of type "ws_genome_id" (A workspace ID that references a
           Genome data object. @id ws KBaseGenomes.Genome
           KBaseGenomeAnnotations.GenomeAnnotation), parameter
           "genomeset_ref" of type "ws_genomeset_id" (A workspace ID that
           references a GenomeSet data object. @id ws KBaseSearch.GenomeSet),
           parameter "out_workspace" of String, parameter "out_tree_id" of
           String, parameter "out_genomeset_ref" of type "ws_genomeset_id" (A
           workspace ID that references a GenomeSet data object. @id ws
           KBaseSearch.GenomeSet), parameter "copy_genomes" of Long,
           parameter "use_ribosomal_s9_only" of Long, parameter
           "nearest_genome_count" of Long
        :returns: instance of type "ws_tree_id" (A workspace ID that
           references a Tree data object. @id ws KBaseTrees.Tree)
        """
        return self._client.call_method(
            'SpeciesTreeBuilder.construct_species_tree',
            [input], self._service_ver, context)

    def find_close_genomes(self, params, context=None):
        """
        Find closely related public genomes based on COG of ribosomal s9 subunits.
        :param params: instance of type "FindCloseGenomesParams" (Input data
           type for find_close_genomes method. Method produces list of
           refereces to public genomes similar to query. query_genome -
           (required) query genome reference max_mismatch_percent -
           (optional) defines maximum mismatch percentage when compare
           aminoacids from user genome with public genomes (defualt value is
           5).) -> structure: parameter "query_genome" of type "ws_genome_id"
           (A workspace ID that references a Genome data object. @id ws
           KBaseGenomes.Genome KBaseGenomeAnnotations.GenomeAnnotation),
           parameter "max_mismatch_percent" of Long
        :returns: instance of list of type "ws_genome_id" (A workspace ID
           that references a Genome data object. @id ws KBaseGenomes.Genome
           KBaseGenomeAnnotations.GenomeAnnotation)
        """
        return self._client.call_method(
            'SpeciesTreeBuilder.find_close_genomes',
            [params], self._service_ver, context)

    def guess_taxonomy_path(self, params, context=None):
        """
        Search for taxonomy path from closely related public genomes (approach similar to find_close_genomes).
        :param params: instance of type "GuessTaxonomyPathParams" (Input data
           type for guess_taxonomy_path method. Method produces taxonomy path
           string. query_genome - (required) query genome reference) ->
           structure: parameter "query_genome" of type "ws_genome_id" (A
           workspace ID that references a Genome data object. @id ws
           KBaseGenomes.Genome KBaseGenomeAnnotations.GenomeAnnotation)
        :returns: instance of String
        """
        return self._client.call_method(
            'SpeciesTreeBuilder.guess_taxonomy_path',
            [params], self._service_ver, context)

    def build_genome_set_from_tree(self, params, context=None):
        """
        :param params: instance of type "BuildGenomeSetFromTreeParams" ->
           structure: parameter "tree_ref" of type "ws_tree_id" (A workspace
           ID that references a Tree data object. @id ws KBaseTrees.Tree),
           parameter "genomeset_ref" of type "ws_genomeset_id" (A workspace
           ID that references a GenomeSet data object. @id ws
           KBaseSearch.GenomeSet)
        :returns: instance of type "ws_genomeset_id" (A workspace ID that
           references a GenomeSet data object. @id ws KBaseSearch.GenomeSet)
        """
        return self._client.call_method(
            'SpeciesTreeBuilder.build_genome_set_from_tree',
            [params], self._service_ver, context)

    def status(self, context=None):
        return self._client.call_method('SpeciesTreeBuilder.status',
                                        [], self._service_ver, context)
