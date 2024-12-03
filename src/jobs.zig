const std = @import("std");

const job = struct {
    title: []u8,
    company: []u8,
    companydesc: []8,

    location: []u8,
    workmode: workmode,
    hours: hours,
    contract: contract,
    salary: salarydetails,

    description: []u8,
    responsibilities: []u8,

    requirements_essential: []u8,
    requirements_desirable: []u8,
    skill_list: []u8,

    hiring_process: []u8,
    requirements_legal: []8,
};

const workmode = enum {
    onsite,
    remote,
    hybrid,
};

const hours = enum {
    fulltime,
    parttime,
};

const contract = enum {
    permanent,
    fixed,
};

const salarydetails = union(enum) {
    none: void,
    value: u32,
    range: salarayrange,
};

const salarayrange = struct {
    min: u32,
    max: u32,
};
