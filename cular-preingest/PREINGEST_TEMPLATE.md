THIS DOCUMENT HAS BEEN GENERATED AUTOMATICALLY
----------------------------------------------

Depositor: **The Division of Rare and Manuscript Collections**  
Collection title: **$COLLECTION_TITLE**  
CULAR title: $CULAR_TITLE**  
Date Finalized:  


Partners
--------
1. **Erin Faulder**, **Digital Archivist**, will represent the depositor.  
2. **Erin Faulder**, **Digital Archivist**, will coordinate licensing, access rights, and make records of this available for deposit. 
3. **Dianne Dietrich**, **Digital Projects Librarian**, will assist in arrangement of the assets and coordination of the deposit according to the plan described below. 
4. **Michelle Paolillo**, **CULAR Service Manager**, will work directly with Dianne to determine the logistics of the flow of assets from current storage into preservation storage.  She will also coordinate the work of the development team to facilitate ingest.


Assets
------
1. Description of assets
    a. Intellectual description: the EAD collection level metadata describes the content, as does the RMC finding aid. Refer to RMC with this citation for more information: $CITATION. Division of Rare and Manuscript Collections, Cornell University Library.
    b. Technical description: The collection consists of files in these versions 
        * $TECH_SPEC_STRING_LIST
2. Designated Community:
    a. Subject tracings are included in the EAD collection level metadata and the RMC finding aid.
3. Rights statement prepared by Copyright Services: 
    a. Contact The Division of Rare and Manuscript Collections for rights associated with this material. 
4. Coordinated copies: 
    a. None.
5. Copies of assets that won’t be coordinated outside of CULAR:
    a. Access copies of assets may exist on The Division of Rare and Manuscript Collection’s shared storage for local retrieval. 
    b. There is currently no preservation strategy for the digital surrogates separate from this plan. 


Deposit structure
-----------------
1. The first level represents the depositor, **RMC**
2. The second level represents the subdivision of RMC, **$RMC_SUBDIVISION** ($RMC_SUBDIVISION_STRING)
3. The third level represents the collection, which is named **$CULAR_TITLE**
    a. Collection-level metadata that describe the assets as an aggregate will be a child object of this aggregate object.
4. The fourth level includes
    a. An aggregate called _Documentation containing any documentation, including 
        * a copy of this plan
        * Spreadsheet with item level metadata
        * $ADDITIONAL_DOCUMENTATION_STRING_LIST
    b. Asset-level aggregates, each containing their master level and derivative files.  


Technical Plan 
--------------
(for use of arrangers and developers; depositors are encouraged to review)  

1. Destination of deposit: 
    a. CULAR-Overflow SFS (archivalXX)/S3; use overflow ingest procedures to create json manifest and ingest appropriately
    b. Metadata, JSON, and _Documentation folder and contents will be ingested into CULAR-Classic 
    c. Destination path is RMC/$CULAR_TITLE
2. Resources:  
    a. Obtain from smb://files.cornell.edu/lib/$RMC_SERVER/$CULAR_TITLE
    b. Aggregate size is $AGGREGATE_SIZE
        * $NUMBER_TYPE_LIST
    c. Ingest as arranged at source
    d. Json manifest for assets is placed directly within this folder.
3. Documentation: The source for the _Documentation folder is smb://files.cornell.edu/lib/CULARIngest/RMC/$CULAR_TITLE
4. Metadata: Collection level metadata will be 
    a. Supplied as EAD XML by the depositor
    b. Named $CULAR_TITLE.xml
    c. Placed in the top level directory of the collection smb://files.cornell.edu/lib/CULARIngest/RMC/$CULAR_TITLE
    d. Json manifest created through ingest will be placed at smb://files.cornell.edu/lib/CULARIngest/RMC/$RMC_SUBDIVISION/$CULAR_TITLE.json
5. Filesystem dates do not need to be captured.
6. The assets do not contain sensitive data.
7. When ingest is complete developers will notify **Dianne Dietrich** who will work with depositor to obtain final signed off.  
8. **Dianne Dietrich** will delete from CULARingest when ingest is completed. **Erin Faulder** will coordinate deletion in other RMCData SFS.  
9. Additional deposits may be expected.