create table if not exists evp.data
(
    id                                         BIGINT auto_increment,
    indx                                       BIGINT null,
    vin                                        varchar(255) null,
    county                                     varchar(255) null,
    city                                       varchar(255) null,
    state                                      varchar(255) null,
    postal_code                                varchar(255) null,
    model_year                                 varchar(255) null,
    make                                       varchar(255) null,
    model                                      varchar(255) null,
    electric_vehicle_type                      varchar(255) null,
    clean_alternative_fuel_vehicle_eligibility varchar(255) null,
    electric_range                             varchar(255) null,
    base_msrp                                  varchar(255) null,
    legislative_district                       varchar(255) null,
    dol_vehicle_id                             varchar(255) null,
    vehicle_location                           varchar(255) null,
    electric_utility                           varchar(255) null,
    census_tract                               varchar(255) null,
    constraint data_pk
        primary key (id)
);