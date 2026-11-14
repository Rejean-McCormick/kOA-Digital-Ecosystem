# DaaT — External source landscape and access lanes

**Status:** `TARGET_DESIGN`. A catalogue entry is a potential integration, **not a deployed connector, licensing permission or completed security review**. The authoritative detailed catalogue is in the DaaT repository `docs/data/source-family-landscape-36.csv`.

## Source market map

| Societal data reservoir | Illustrative sources | Typical shape | Access lanes |
|---|---|---|---|
| Scientific publication and academic archives | DOI registries, academic index, institutional repositories | OAI-PMH/XML, RIS/BibTeX, metadata JSON, authorized PDF | Harvest/API, snapshot, reference |
| Public knowledge and language resources | Wikidata, taxonomies, ontologies and encyclopedias | RDF/JSON, SPARQL, wiki export | Bulk/API/reference |
| Documents and archives | Personal/enterprise PDF, Office, ZIP, museums and libraries | Files, metadata, image/text and OCR references | Local artifacts, bulk |
| Software and technical collaboration | GitHub, GitLab, issues and repositories | Git trees, commits, source files, JSON API | Versioned tree, API |
| Business transactions | Acomba, ERP, CRM, inventory and payment exports | SDK/ODBC/SQL, CSV, API, accounting events | Enterprise DB/API/snapshot |
| Government and legal data | public datasets, statistics, case law, registers | CSV/JSON/Parquet, PDF, XML | API, harvest, bulk |
| Enterprise platforms | SQL databases, cloud documents, data lakes | SQL/CDC, Parquet, object versions | DB/bulk/stream |
| Geospatial and environmental | OSM, GeoJSON, GIS, weather and Earth observations | PBF/GeoJSON/NetCDF/HDF5 | Bulk/API/stream |
| Health and research instruments | FHIR/HL7, clinical documents, lab exports | FHIR JSON, XML, DICOM, instrument files | Authorized API/snapshot, isolated import |
| Industrial and sensor networks | maintenance systems, IoT, SCADA | OPC UA/MQTT, measurements, events | Stream/DB |
| Communications and civic evidence | Consent-based exports, submissions, discussion archives | EML/JSON/CSV, transcripts/media | API/local artifacts |
| Media and creative archives | audio, video, image libraries | IIIF, media files, metadata and subtitles | Local/bulk/API |

These are **groups of the 36 research families**, not a replacement/renumbering of the DaaT CSV. Multiple access lanes and content archetypes can apply to one provider.

## Practical starting points

**First:** local PDF and Git source snapshots, with safely bounded extraction and exact page/commit references. **Next:** legally permitted scholarly metadata and private read-only Acomba sandbox. **Later:** enterprise CDC, streaming and large-volume engines after durable replay/security review.

The selection should minimize copying and exposure. `Reference-only` may be the correct terminal result when source terms prohibit mirroring. A source content type does not automatically imply an Arketype template or authority to create a canonical Kristal.

## Cross-owner handling

C0 documents scope only. DaaT selects a route; Skope/source adapters collect where authorized; Médiathèque owns any accepted custody; DaaT applies adopted mappings/admission; Kristalizer/diK support review; Arketype suggests design; Framework/Kit author; independent owners qualify and release. IK and receiving products enforce adopted interaction contracts.

See [authority](authority-and-handoffs.md), [qualification](qualification-and-delivery.md) and [FC-23](../functional-chains/chains/FC-23-external-interop.md).
