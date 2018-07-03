THIS DOCUMENT HAS BEEN GENERATED AUTOMATICALLY
----------------------------------------------

Depositor: **$DEPOSITOR**
Collection title: **$COLLECTION_TITLE**  
CULAR title: **$CULAR_TITLE**  
Date Finalized:  


Partners
--------
* $PARTNER_STRING_LIST
* **Dianne Dietrich**, **Digital Projects Librarian**, will assist in arrangement of the assets and coordination of the deposit according to the plan described below. 
* **Michelle Paolillo**, **CULAR Service Manager**, will work directly with Dianne to determine the logistics of the flow of assets from current storage into preservation storage.  She will also coordinate the work of the development team to facilitate ingest.


Assets
------
1. Description of assets
    a. Intellectual description: $INTELLECTUAL_DESCRIPTION_STRING
    b. Technical description: The collection consists of files in these versions 
        * $TECH_SPEC_STRING_LIST
2. Designated Community:
    a. $DESIGNATED_COMMUNITY_STRING
3. Rights statement prepared by Copyright Services: 
    a. $COPYRIGHT_STRING
4. Coordinated copies: 
    a. $COORDINATED_COPIES_STRING
5. Copies of assets that won’t be coordinated outside of CULAR:
    a. There is currently no preservation strategy for the digital surrogates separate from this plan. 


Deposit structure
-----------------
1. The first level represents the depositor, **$DEPOSITOR**
2. The second level represents the collection, which is named **$CULAR_TITLE**
    a. Collection-level metadata that describe the assets as an aggregate will be a child object of this aggregate object.
4. The third level includes
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
    c. Destination path is $DEPOSITOR/$CULAR_TITLE
2. Resources:  
    a. Obtain from smb://files.cornell.edu/lib/$ASSETS_SERVER/$CULAR_TITLE
    b. Aggregate size is $AGGREGATE_SIZE
        * $NUMBER_TYPE_LIST
    c. Ingest as arranged at source
    d. Json manifest for assets is placed directly within this folder.
3. Documentation: The source for the _Documentation folder is smb://files.cornell.edu/lib/CULARIngest/$DEPOSITOR/$CULAR_TITLE
4. Metadata: Collection level metadata will be 
    a. Collection level metadata will be supplied in XLSX format, to be walked to EAD XML by the script created and maintained by CULAR developers. The resulting XML will be ingested as a metadata object for the collection aggregate. The file will be named $CULAR_TITLE.xlsx
    c. Placed in the top level directory of the collection smb://files.cornell.edu/lib/CULARIngest/$DEPOSITOR/$CULAR_TITLE
    d. Json manifest created through ingest will be placed at smb://files.cornell.edu/lib/CULARIngest/$DEPOSITOR/$CULAR_TITLE.json
5. Filesystem dates **do / do not** need to be captured.
6. The assets **do / do not** contain sensitive data.
7. When ingest is complete developers will notify **Dianne Dietrich** who will work with depositor to obtain final signed off.  
8. **Dianne Dietrich** will delete from CULARingest when ingest is completed and coordinate deletion on $ASSETS_SERVER.
9. Additional deposits **may / may not** be expected.
