<?xml version='1.0' encoding="UTF-8"?>
<xsl:stylesheet	version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:html="http://www.w3.org/1999/xhtml" xmlns="http://www.w3.org/1999/xhtml">

    <xsl:output method="xml" omit-xml-declaration="no"/>

    <xsl:template match="node()|@*">
        <xsl:copy>
            <xsl:apply-templates select="@*|node()"/>
        </xsl:copy>
    </xsl:template>

    <xsl:template match="html:div[@class = 'chapter' or @class = 'page'  or starts-with(@class, 'sect')]">
        <xsl:apply-templates/>
    </xsl:template>

</xsl:stylesheet>
