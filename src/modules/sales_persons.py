sales_persons_dict = {
    "Lazada" : {
        "Jabra" : {
            "name" : "LAZADA-JABRA",
            "filename" : "JABRA PH",
            "debtor" : "102-J001"
        },
        # fix the following below
        "LG Monitors" : {
            "name" : "LG-ONLINE SALES",
            "filename" : "LAZADA LG",
            "debtor" : "102-L001"
        },
        "ADDASOUND Audio" : {
            "name" : "LAZADA ADDA",
            "filename" : "LAZADA ADDA",
            "debtor" : "103-A00000018"
        },
        "Afford4C" : {
            "name" : "LAZADA AFFORD",
            "filename" : "AFFORD",
            "debtor" : "103-V001"
        },
        "Poly Enterprise" : {
            "name" : "LAZADA POLYCOM",
            "filename" : "POLY",
            "debtor" : "103-P00000006"
        },
        "LAZADA-KONTROLFREEK" : { # this is right
            "name" : "KONTROLFREEK PH - ONLINE SALES",
            "filename" : "LAZADA KONTROLFREEK",
            "debtor" : "103-K00000011"
        }
    },
    "Shopee" : {
        "Jabra" : {
            "name" : "SHOPEE-JABRA ONLINE",
            "debtor" : "102-S001"
        }
    }
}

# Flat dict for SiteGiant exports.
# Keys match the full `marketplace` string as exported by SiteGiant.
sitegiant_marketplace_dict = {
    # --- Lazada ---
    "Lazada Jabra" : {
        "name"     : "LAZADA-JABRA",
        "filename" : "JABRA PH",
        "debtor"   : "102-J001"
    },
    "Lazada JLab" : {
        "name"     : "TODO: LAZADA-JLAB SALESPERSON",
        "filename" : "JLAB PH",
        "debtor"   : "TODO: LAZADA-JLAB DEBTOR"
    },
    # --- Shopee ---
    "Shopee Jabra" : {
        "name"     : "SHOPEE-JABRA ONLINE",
        "filename" : "JABRA PH",
        "debtor"   : "102-S001"
    },
    "Shopee Afford4C" : {
        "name"     : "LAZADA AFFORD",      # reuse existing
        "filename" : "AFFORD",
        "debtor"   : "103-V001"
    },
    "Shopee Jlab" : {
        "name"     : "TODO: SHOPEE-JLAB SALESPERSON",
        "filename" : "JLAB PH",
        "debtor"   : "TODO: SHOPEE-JLAB DEBTOR"
    },
    "Shopee HP Poly" : {
        "name"     : "TODO: SHOPEE-HP POLY SALESPERSON",
        "filename" : "HP POLY PH",
        "debtor"   : "TODO: SHOPEE-HP POLY DEBTOR"
    },
    "Shopee TP-Link Verified Store" : {
        "name"     : "TODO: SHOPEE-TPLINK SALESPERSON",
        "filename" : "TPLINK PH",
        "debtor"   : "TODO: SHOPEE-TPLINK DEBTOR"
    },
    # --- TikTok ---
    "Tiktok Jabra" : {
        "name"     : "TODO: TIKTOK-JABRA SALESPERSON",
        "filename" : "JABRA PH",
        "debtor"   : "TODO: TIKTOK-JABRA DEBTOR"
    },
}
