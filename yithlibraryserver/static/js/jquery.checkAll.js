// Yith Library Server is a password storage server.
// Copyright (C) 2015 Lorenzo Gil Sanchez <lorenzo.gil.sanchez@gmail.com>
//
// This file is part of Yith Library Server.
//
// Yith Library Server is free software: you can redistribute it and/or modify
// it under the terms of the GNU Affero General Public License as published by
// the Free Software Foundation, either version 3 of the License, or
// (at your option) any later version.
//
// Yith Library Server is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU General Public License for more details.
//
// You should have received a copy of the GNU Affero General Public License
// along with Yith Library Server.  If not, see <http://www.gnu.org/licenses/>.

(function ($) {
    "use strict";

    $.fn.checkAll = function (options) {
        return this.each(function () {

            $(this).click(function (event) {
                var isChecked = $(this).is(":checked"),
                    $inputs = $("table input[type='checkbox']:not([disabled])");

                $inputs.prop("checked", isChecked);

            });
        });
    };

}(jQuery));
