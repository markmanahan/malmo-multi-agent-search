//
// This file was generated by the JavaTM Architecture for XML Binding(JAXB) Reference Implementation, v2.2.4 
// See <a href="http://java.sun.com/xml/jaxb">http://java.sun.com/xml/jaxb</a> 
// Any modifications to this file will be lost upon recompilation of the source schema. 
// Generated on: 2018.09.10 at 03:51:00 PM EDT 
//


package com.microsoft.Malmo.Schemas;

import javax.xml.bind.annotation.XmlAccessType;
import javax.xml.bind.annotation.XmlAccessorType;
import javax.xml.bind.annotation.XmlAttribute;
import javax.xml.bind.annotation.XmlElement;
import javax.xml.bind.annotation.XmlRootElement;
import javax.xml.bind.annotation.XmlType;


/**
 * <p>Java class for anonymous complex type.
 * 
 * <p>The following schema fragment specifies the expected content contained within this class.
 * 
 * <pre>
 * &lt;complexType>
 *   &lt;complexContent>
 *     &lt;restriction base="{http://www.w3.org/2001/XMLSchema}anyType">
 *       &lt;all>
 *         &lt;element name="ModifierList" minOccurs="0">
 *           &lt;complexType>
 *             &lt;complexContent>
 *               &lt;restriction base="{http://ProjectMalmo.microsoft.com}CommandListModifier">
 *                 &lt;choice maxOccurs="unbounded">
 *                   &lt;element name="command" type="{http://ProjectMalmo.microsoft.com}DiscreteMovementCommand" maxOccurs="unbounded" minOccurs="0"/>
 *                 &lt;/choice>
 *               &lt;/restriction>
 *             &lt;/complexContent>
 *           &lt;/complexType>
 *         &lt;/element>
 *       &lt;/all>
 *       &lt;attribute name="autoFall" type="{http://www.w3.org/2001/XMLSchema}boolean" default="false" />
 *       &lt;attribute name="autoJump" type="{http://www.w3.org/2001/XMLSchema}boolean" default="false" />
 *     &lt;/restriction>
 *   &lt;/complexContent>
 * &lt;/complexType>
 * </pre>
 * 
 * 
 */
@XmlAccessorType(XmlAccessType.FIELD)
@XmlType(name = "", propOrder = {

})
@XmlRootElement(name = "DiscreteMovementCommands")
public class DiscreteMovementCommands {

    @XmlElement(name = "ModifierList")
    protected DiscreteMovementCommands.ModifierList modifierList;
    @XmlAttribute(name = "autoFall")
    protected Boolean autoFall;
    @XmlAttribute(name = "autoJump")
    protected Boolean autoJump;

    /**
     * Gets the value of the modifierList property.
     * 
     * @return
     *     possible object is
     *     {@link DiscreteMovementCommands.ModifierList }
     *     
     */
    public DiscreteMovementCommands.ModifierList getModifierList() {
        return modifierList;
    }

    /**
     * Sets the value of the modifierList property.
     * 
     * @param value
     *     allowed object is
     *     {@link DiscreteMovementCommands.ModifierList }
     *     
     */
    public void setModifierList(DiscreteMovementCommands.ModifierList value) {
        this.modifierList = value;
    }

    /**
     * Gets the value of the autoFall property.
     * 
     * @return
     *     possible object is
     *     {@link Boolean }
     *     
     */
    public boolean isAutoFall() {
        if (autoFall == null) {
            return false;
        } else {
            return autoFall;
        }
    }

    /**
     * Sets the value of the autoFall property.
     * 
     * @param value
     *     allowed object is
     *     {@link Boolean }
     *     
     */
    public void setAutoFall(Boolean value) {
        this.autoFall = value;
    }

    /**
     * Gets the value of the autoJump property.
     * 
     * @return
     *     possible object is
     *     {@link Boolean }
     *     
     */
    public boolean isAutoJump() {
        if (autoJump == null) {
            return false;
        } else {
            return autoJump;
        }
    }

    /**
     * Sets the value of the autoJump property.
     * 
     * @param value
     *     allowed object is
     *     {@link Boolean }
     *     
     */
    public void setAutoJump(Boolean value) {
        this.autoJump = value;
    }


    /**
     * <p>Java class for anonymous complex type.
     * 
     * <p>The following schema fragment specifies the expected content contained within this class.
     * 
     * <pre>
     * &lt;complexType>
     *   &lt;complexContent>
     *     &lt;restriction base="{http://ProjectMalmo.microsoft.com}CommandListModifier">
     *       &lt;choice maxOccurs="unbounded">
     *         &lt;element name="command" type="{http://ProjectMalmo.microsoft.com}DiscreteMovementCommand" maxOccurs="unbounded" minOccurs="0"/>
     *       &lt;/choice>
     *     &lt;/restriction>
     *   &lt;/complexContent>
     * &lt;/complexType>
     * </pre>
     * 
     * 
     */
    @XmlAccessorType(XmlAccessType.FIELD)
    @XmlType(name = "")
    public static class ModifierList
        extends CommandListModifier
    {


    }

}
