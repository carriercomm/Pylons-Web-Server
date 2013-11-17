<!--
 Dan Robinson
 0700662
-->
<%namespace name="commonFunctions" file="commonFunctions.mako"/>
<html>
${commonFunctions.head()}
<body>
	<div class="pageContent">
		${commonFunctions.nav()}
		<div class="mainContent">
      <div id="imageSlider">
          <div class="loading"><img src="/img/ajax-loader.gif" alt="loading..."/></div>
          <div class="carousel-inner">
          </div>
       </div>
      <div class="raised">
			 <h1>${c.username} Dashboard</h1>
       <form role="form" id="searchForm" name="searchForm">
        <div class="form-group">
          <input type="text" class="form-control" id="searchTerm" placeholder="Enter a term to search" />
        </div>
        <div class="form-group">
          <label for="numResults" class="control-label" style="color: white;">Number of results to display:</label>
          <select id="numResults" class="form-control">
            <option>1</option>
            <option>2</option>
            <option>5</option>
            <option>10</option>
            <option>15</option>
          </select>
        </div>
        <div class="form-group">
          <button type="submit" class="btn btn-success">Search</button>
        </div>
      </form>
       <!-- <button class="btn btn-success" onclick='rotateDiv($(".spiral"));''>Spin!</button> -->
      </div>
		</div>
		${commonFunctions.footer()}
	</div>
</body>
</html>
