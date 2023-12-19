// Hide submenus
$('#body-row .collapse').collapse('hide');

// Collapse/Expand icon
$('#collapse-icon').addClass('fa-angle-double-left');

// Collapse click
$('[data-toggle=sidebar-collapse]').click(function () {
  SidebarCollapse(false);
});

$('.content').click(function () {
  SidebarCollapse(true);
});

function SidebarCollapse(content_clicked) {
  if (content_clicked) {
    $('.content').removeClass('masked');
    $('.content').addClass('d-none');
    $('.menu-collapsed').addClass('d-none');
    $('.sidebar-submenu').addClass('d-none');
    $('.submenu-icon').addClass('d-none');
  } else {
    $('.content').toggleClass('masked');
    $('.content').toggleClass('d-none');
    $('.menu-collapsed').toggleClass('d-none');
    $('.sidebar-submenu').toggleClass('d-none');
    $('.submenu-icon').toggleClass('d-none');
  }

  $('#sidebar-container').toggleClass('sidebar-collapsed sidebar-expanded');
  // Treating d-flex/d-none on separators with title
  var SeparatorTitle = $('.sidebar-separator-title');
  if (SeparatorTitle.hasClass('d-flex')) {
    SeparatorTitle.removeClass('d-flex');
  } else {
    SeparatorTitle.addClass('d-flex');
  }

  // Collapse/Expand icon
  $('#collapse-icon').toggleClass('fa-angle-double-right fa-angle-double-left');
}

$(document).ready(function () {

  $("#search-anywhere-0").on("keyup", function () {
    var value = $(this).val().toLowerCase();
    $("#search-section-0 .card").filter(function () {
      $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
    });
  });

  $("#search-anywhere-11").on("keyup", function () {
    var value = $(this).val().toLowerCase();
    $("#search-section-11 .card").filter(function () {
      $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
    });
  });

  $("#search-anywhere-12").on("keyup", function () {
    var value = $(this).val().toLowerCase();
    $("#search-section-12 .card").filter(function () {
      $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
    });
  });

  $("#search-anywhere-13").on("keyup", function () {
    var value = $(this).val().toLowerCase();
    $("#search-section-13 .card").filter(function () {
      $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
    });
  });

  $("#search-anywhere-14").on("keyup", function () {
    var value = $(this).val().toLowerCase();
    $("#search-section-14 .card").filter(function () {
      $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
    });
  });

  $("#search-anywhere-15").on("keyup", function () {
    var value = $(this).val().toLowerCase();
    $("#search-section-15 .card").filter(function () {
      $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
    });
  });

  $("#search-anywhere-2").on("keyup", function () {
    var value = $(this).val().toLowerCase();
    $("#search-section-2 .card").filter(function () {
      $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
    });
  });

  $("#search-anywhere-7").on("keyup", function () {
    var value = $(this).val().toLowerCase();
    $("#search-section-7 .card").filter(function () {
      $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
    });
  });

});
