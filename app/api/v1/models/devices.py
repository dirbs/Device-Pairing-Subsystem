"""
DPS Devices Model package.
Copyright (c) 2018 Qualcomm Technologies, Inc.
 All rights reserved.
 Redistribution and use in source and binary forms, with or without modification, are permitted (subject to the
 limitations in the disclaimer below) provided that the following conditions are met:
 * Redistributions of source code must retain the above copyright notice, this list of conditions and the following
 disclaimer.
 * Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following
 disclaimer in the documentation and/or other materials provided with the distribution.
 * Neither the name of Qualcomm Technologies, Inc. nor the names of its contributors may be used to endorse or promote
 products derived from this software without specific prior written permission.
 NO EXPRESS OR IMPLIED LICENSES TO ANY PARTY'S PATENT RIGHTS ARE GRANTED BY THIS LICENSE. THIS SOFTWARE IS PROVIDED BY
 THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
 THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
 COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
 DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS;
 OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR
 TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
 POSSIBILITY OF SUCH DAMAGE.
"""

from app import db


class Devices(db.Model):
    """ Class to create Db Table devices """

    id = db.Column(db.BigInteger, primary_key=True)
    model = db.Column(db.String(1000))
    brand = db.Column(db.String(1000))
    serial_no = db.Column(db.String(1000))
    mac = db.Column(db.String(50))
    rat = db.Column(db.String(50))

    owner_id = db.Column(db.BigInteger, db.ForeignKey('owner.id'))

    pairing_codes = db.relationship('Pairing_Codes', backref='devices', lazy='dynamic')
    imeis = db.relationship('Imei', backref='devices', lazy='dynamic')

    def __repr__(self):     # pragma: no cover
        return "<Devices ({} ,{}, {})>".format(self.id, self.model, self.brand)

    @classmethod
    def create_index(cls, engine):
        """ Method to create Indexes for devices table. """

        devices_serialno = db.Index('devices_serialno_index', cls.serial_no, postgresql_concurrently=False)
        devices_serialno.create(bind=engine)

        devices_mac = db.Index('devices_mac_index', cls.mac, postgresql_concurrently=False)
        devices_mac.create(bind=engine)

        devices_model = db.Index('devices_model_index', cls.model, postgresql_concurrently=False)
        devices_model.create(bind=engine)

        devices_brand = db.Index('devices_brand_index', cls.brand, postgresql_concurrently=False)
        devices_brand.create(bind=engine)
